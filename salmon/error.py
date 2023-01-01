from salmon.bounce import COMBINED_STATUS_CODES, PRIMARY_STATUS_CODES, SECONDARY_STATUS_CODES

class SMTPError(Exception):
    """
    You can raise this error when you want to abort with a SMTP error code to
    the client.  This is really only relevant when you're using the
    SMTPReceiver and the client understands the error.

    If you give a message than it'll use that, but it'll also produce a
    consistent error message based on your code.  It uses the errors in
    salmon.bounce to produce them.
    """
    def __init__(self, code, message=None):
        self.code = code
        self.message = message or self.error_for_code(code)

        Exception.__init__(self, "%d %s" % (self.code, self.message))

    def error_for_code(self, code):
        primary, secondary, tertiary = str(code)

        primary = PRIMARY_STATUS_CODES.get(primary, "")
        secondary = SECONDARY_STATUS_CODES.get(secondary, "")
        combined = COMBINED_STATUS_CODES.get(primary + secondary, "")

        return " ".join([primary, secondary, combined]).strip()
