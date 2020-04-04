import psycopg2

class PostgisUtil:

    def __init__(self):
        try:
            self.cur = None
            self.initConn()
        except:
            print("postgis is unavailable")

    def initConn(self):
        conn = psycopg2.connect(host="postgis",database="2TICKET", user="dbuser", password="dbpass")
        self.cur = conn.cursor()

    def getEvents(self, latitude, longitude, date, distance = 5.0):

        if self.cur is None:
            self.initConn()

        self.cur.execute(
            "select places.id, \
                   places.date, \
                    places.description, \
                    places.latitude, \
                    places.longitude \
            from (\
                select e.id, \
                    e.date, \
                e.description, \
                p.latitude, \
                p.longitude, \
                ST_DISTANCE(ST_POINT(%f,%f), ST_POINT(p.latitude, p.longitude))*100 AS distanceInKM \
                    from \
                        event e \
                        inner join place p \
                        on e.id_place = p.id \
                        ) places \
                WHERE distanceInKM < %f \
                    AND date > to_date('%s', 'YYYYMMDD') \
                   ORDER BY places.date ;" % (latitude, longitude, distance, date))
        return self.cur.fetchall()