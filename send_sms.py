from twilio.rest import Client

from credentials import (
			account_id, 
			auth_token, 
			my_cell, 
			my_twilio
		)

client = Client(account_id, auth_token)


message = client.messages.create(
				body = 'Keep social distance. Be real hero.',
				from_ = my_twilio,
				to = my_cell
			)

print(message.sid)