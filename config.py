from letter import Letter
from santa import Santa

################################################################################
# SMTP configuration settings.
################################################################################
smtp_user = 'username'
smtp_pass = 'password'
smtp_host = 'email-smtp.example.com'
smtp_port = 587
from_email = 'email-used-to-send-letters@example.com'

################################################################################
# This the secret santa letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automatically replaced by the secret
# santa's name, and his/her recipient of their gift.
################################################################################
letter = Letter(
    from_name='Secret Santa',
    from_email=from_email,
    subject='Family Christmas',
    body="""
Ho Ho Ho!

{santa}, you are {recipient}'s secret Santa!

Merry Christmas!
"""
)

################################################################################
# The complete list of all the secret santa's and their email addresses.
################################################################################
santas = [
    Santa('James',      'james@example.com'),
    Santa('Mary',       'mary@example.com'),
    Santa('Nancy',      'nancy@example.com'),
    Santa('John',       'john@example.com'),
    Santa('Michael',    'michael@example.com'),
    Santa('Lisa',       'lisa@example.com'),
    Santa('David',      'david@example.com'),
    Santa('Linda',      'linda@example.com'),
]

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {
    # Do not allow James to be santa for Mary
    'James': ('Mary',),

    # Do not allow Mary to be santa for James
    'Mary': ('James',),

    # Do not allow Nancy to be santa for John or Mary
    'Nancy': ('John', 'Mary',),

    # Something like below is bad, Linda can't be a secret santa for anyone!
#   'Linda': ('James', 'Mary', 'Nancy', 'John', 'Michael', 'Lisa', 'David'),
}

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
record_file = 'secret-santa-email-record.txt'
