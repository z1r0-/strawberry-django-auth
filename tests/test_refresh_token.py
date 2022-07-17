from .testCases import DefaultTestCase, RelayTestCase


class RefreshTokenTestCaseMixin:
    def setUp(self):
        self.user = self.register_user(
            email="foo@email.com", username="foo", verified=True, archived=False
        )

    def test_refresh_token(self):
        query = self.login_query()
        executed = self.make_request(query=query)
        assert executed["obtainPayload"]["refreshToken"]

        query = self.get_verify_query(executed["obtainPayload"]["refreshToken"])
        executed = self.make_request(query=query)
        assert executed["success"]
        self.assertTrue(executed["refreshPayload"]["refreshToken"])
        self.assertTrue(executed["refreshPayload"]["payload"])
        assert not executed["errors"]

    def test_invalid_token(self):
        query = self.get_verify_query("invalid_token")
        executed = self.make_request(query=query)
        assert not executed["success"]
        self.assertFalse(executed["refreshPayload"])
        assert executed["errors"]


class RefreshTokenTestCase(RefreshTokenTestCaseMixin, DefaultTestCase):
    def get_verify_query(self, token):
        return """
        mutation {
        refreshToken(refreshToken: "%s" )
            {
            refreshPayload{
              payload{
                exp
                origIat
                username
              }
              token
              refreshToken
              refreshExpiresIn
            }
            errors
                success
          }
        }
        """ % (
            token
        )


class RefreshTokenRelayTestCase(RefreshTokenTestCaseMixin, RelayTestCase):
    def get_verify_query(self, token):
        return """
        mutation {
        refreshToken(input: {refreshToken: "%s"} )
            {
            refreshPayload{
              payload{
                exp
                origIat
                username
              }
              token
              refreshToken
              refreshExpiresIn
            }
            errors
            success
          }
        }
        """ % (
            token
        )
