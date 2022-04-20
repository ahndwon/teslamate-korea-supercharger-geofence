import csv
import logging
import os

import requests
from bs4 import BeautifulSoup

from datetime import datetime
from decouple import config

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

API_KEY = config('API_KEY')
today_date = datetime.now().strftime('%Y-%m-%d')


class SuperCharger:
    def __init__(self, name, address, lat=0, lng=0):
        self.name = name
        self.address = address
        self.lat = lat
        self.lng = lng


class Crawler:
    y_m_d__h_m_s = '%Y-%m-%d_%H:%M:%S'

    def __init__(self, url):
        self.url = url

    @staticmethod
    def get_geocode(address):
        formatted = address.replace(' ', '+')
        geocode_json = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?address={formatted}&key={API_KEY}').json()
        logging.info(f'geocode: {geocode_json}')
        return geocode_json

    @staticmethod
    def download_url(url):
        return requests.get(url).text

    @staticmethod
    def search_backup(name):
        with open('address_backup.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                logging.info(f'row: {row}')
                if row[0] == name:
                    return row[2], row[3]
            raise Exception(f'charger not found : {name}')

    @staticmethod
    def search_latest_saved_superchargers_file(self, directory):
        files = []
        for file in os.listdir(directory):
            if file.startswith("superchargers"):
                files.append(file)
                logging.info(f'latest supercharger file : {file}')

        return \
            sorted(files, key=lambda x: datetime.strptime(x.lstrip("superchargers_").rstrip(".csv"), self.y_m_d__h_m_s),
                   reverse=True)[0]

    @staticmethod
    def read_saved_superchargers(self, directory):
        file = self.search_latest_saved_superchargers_file(self, directory)
        saved_superchargers = []
        with open(f'{directory}/{file}') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # skip header
            next(reader)
            for row in reader:
                logging.info(f'row: {row}')
                saved_superchargers.append(row[0])

        return saved_superchargers

    @staticmethod
    def check_new_supercharger(new_list, old_list):
        chargers_to_remove = []
        chargers = new_list.copy()
        for s in old_list:
            for n in new_list:
                if n.name == s:
                    chargers_to_remove.append(n)

        logging.info(f'chargers_to_remove {len(chargers_to_remove)}: {chargers_to_remove}')

        for s in chargers_to_remove:
            chargers.remove(s)

        return chargers

    @staticmethod
    def parse_supercharger_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        superchargers = []
        # superchargers_not_found = []
        superchargers_coming_soon = 0
        for vcard in soup.find_all('address', 'vcard'):
            charger_name = vcard.find('a').text
            address = vcard.findNext('span', 'street-address').text.strip()
            logging.info(f'{charger_name}, {address}')
            if not charger_name.endswith('(coming soon)'):
                superchargers.append(SuperCharger(charger_name, address))

            else:
                superchargers_coming_soon += 1

        logging.info(f'superchargers current count: {len(superchargers)}')
        logging.info(f'superchargers coming soon count: {superchargers_coming_soon}')
        return superchargers

    @staticmethod
    def add_street_address(self, superchargers):
        logging.info(f'superchargers {len(superchargers)}: {superchargers}')

        superchargers_not_found = []
        for sc in superchargers:
            geocode = self.get_geocode(sc.address)
            logging.info(f'geocode: {geocode}')

            results = geocode['results']
            if not len(results) == 0:
                location = geocode['results'][0]['geometry']['location']
                sc.lat = location['lat']
                sc.lng = location['lng']
            else:
                try:
                    lat, lng = self.search_backup(sc.name)
                    sc.lat = lat
                    sc.lng = lng
                except Exception:
                    logging.exception(f'Failed to get location: {sc.name}, {sc.address}')
                    superchargers_not_found.append(SuperCharger(sc.name, sc.address))
        return superchargers, superchargers_not_found

    @staticmethod
    def write_chargers(self, superchargers, directory, prefix):
        date = datetime.now().strftime(self.y_m_d__h_m_s)
        file_path = f'{directory}/{prefix}_{date}.csv'
        f = open(file_path, 'x')

        writer = csv.writer(f)

        header = ['name', 'address', 'lat', 'lng']
        writer.writerow(header)
        for s in superchargers:
            row = [s.name, s.address, s.lat, s.lng]
            writer.writerow(row)
        f.close()
        return file_path

    @staticmethod
    def write_sql(self, superchargers, directory, prefix):
        date = datetime.now().strftime(self.y_m_d__h_m_s)
        today_date = datetime.now().strftime('%Y-%m-%d')
        cost_per_unit = 313
        radius = 150
        session_fee = 1000
        file_path = f'{directory}/{prefix}_{today_date}.md'
        f = open(file_path, 'w')

        for s in superchargers:
            sql = f'INSERT INTO public.geofences ' \
                  '(name, latitude, longitude, radius, inserted_at, updated_at, cost_per_unit, session_fee) ' \
                  f'VALUES (\'{s.name}\', {s.lat}, {s.lng}, {radius}, \'{date}\', \'{date}\', ' \
                  f'{cost_per_unit}, {session_fee}) ' \
                  f'ON CONFLICT (name) ' \
                  f'DO UPDATE ' \
                  f'SET name = \'{s.name}\', latitude =  {s.lat}, longitude = {s.lng}, radius = {radius}, ' \
                  f'inserted_at = \'{date}\', updated_at = \'{date}\', cost_per_unit = {cost_per_unit}, ' \
                  f'session_fee = {session_fee}'
            f.write(sql)
            f.write('\n')
            f.write('\n')
        f.close()
        return file_path

    @staticmethod
    def write_change_log(new_chargers, directory, prefix):
        file_path = f'{directory}/{prefix}_{today_date}.md'
        f = open(file_path, 'w')

        f.write('추가된 수퍼차저\n')
        index = 0
        for s in new_chargers:
            index += 1
            f.write(f'{index}. {s.name}\n')
        f.close()
        return file_path

    @staticmethod
    def write_not_found(self, superchargers):
        date = datetime.now().strftime(self.y_m_d__h_m_s)
        f = open(f'./location_not_found_{date}.csv', 'x')

        writer = csv.writer(f)

        header = ['name', 'address', 'lat', 'lng']
        writer.writerow(header)
        for s in superchargers:
            row = [s.name, s.address, s.lat, s.lng]
            writer.writerow(row)
        f.close()

    def crawl(self, url):
        html = self.download_url(url)
        superchargers = self.parse_supercharger_info(self, html)
        logging.info(f'superchargers {len(superchargers)}: {superchargers}')
        old_superchargers = self.read_saved_superchargers(self, "./chargers")
        logging.info(f'old_superchargers {len(old_superchargers)}: {old_superchargers}')
        new_chargers = self.check_new_supercharger(superchargers, old_superchargers)
        logging.info(f'new_chargers {len(new_chargers)}')
        for n in new_chargers:
            logging.info(f'new_charger : {n.name}')

        if len(new_chargers) == 0:
            logging.info(f'no new superchargers')
            return

        superchargers_with_location, superchargers_not_found = self.add_street_address(self, superchargers)
        logging.info(f'superchargers_with_location {len(superchargers_with_location)}: {superchargers_with_location}')
        logging.info(f'superchargers_not_found {len(superchargers_not_found)}: {superchargers_not_found}')

        if len(superchargers_with_location) == 0:
            logging.error(f'geocode failed...')
            return

        if len(superchargers_not_found) != 0:
            logging.error(f'there are superchargers that geocode can\'t get lat, lng. '
                          f'Please add them manually to address_backup.csv')
            return

        self.write_chargers(self, superchargers, "./chargers", "superchargers")
        self.write_sql(self, superchargers, "./geofence", "supercharger_geofence")
        self.write_change_log(new_chargers, "./changelogs", "changelogs")

    def run(self):
        logging.info(f'Crawling: {self.url}')
        try:
            self.crawl(self.url)
        except Exception:
            logging.exception(f'Failed to crawl: {self.url}')


if __name__ == '__main__':
    supercharger_kor_url = 'https://www.tesla.com/ko_KR/findus/list/superchargers/South%20Korea'
    Crawler(supercharger_kor_url).run()
