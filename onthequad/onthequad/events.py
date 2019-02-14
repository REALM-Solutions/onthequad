import falcon


class Event:

    def on_get(self, req, resp):
        print("To remove errors")

    def on_post(self, req, resp):
        print("Removing all them red lines")
