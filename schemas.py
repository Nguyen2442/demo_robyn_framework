from pydantic import BaseModel, validator, root_validator

class FruitPostModel(BaseModel):
	name: str

	@validator('name')
	def check_name(cls, value):
		if value == "Banana":
			print("No More Banana!!!")
			raise ValueError('No More Banana!!!')
		return value


