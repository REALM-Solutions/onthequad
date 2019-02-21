import json, falcon


class User:

    def on_get(self, req, resp):
        print("To remove errors")

    """def on_post(self, req, resp):
        print("Removing all them red lines")

        data = json.loads(req.stream.read())
        id = 
        fname = data["body"].firstName
        lname = data["body"].lastName

        user = User(fname: fname, )

        success = database.sendUser(user)

        if success {
        resp.status = falcon.HTTP_200
        resp.body = user
        }
        else {
            resp.status = falcon.HTTP_401
        }
        """

