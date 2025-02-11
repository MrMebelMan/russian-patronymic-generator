# Russian Patronymic Generator
A Python tool that generates male and female Russian patronymics from father's first name using linguistic rules.

If you're a Russian national and want to use this software, better go check the [LICENSE](LICENSE.txt) first.

## Usage

```python3
from patronymic import generate_patronymic

generate_patronymic("Пётр", "male") # Петрович
generate_patronymic("Пётр", "female") # Петровна

generate_patronymic("Павел", "male") # Павлович
generate_patronymic("Павел", "female") # Павловна

generate_patronymic("Георгий", "male") # Георгиевич
generate_patronymic("Георгий", "female") # Георгиевна

generate_patronymic("Валентин", "male") # Валентинович
generate_patronymic("Валентин", "female") # Валентиновна

generate_patronymic("Еремей", "male") # Еремеевич
generate_patronymic("Еремей", "female") # Еремеевна

generate_patronymic("Савелий", "male") # Савельевич
generate_patronymic("Савелий", "female") # Савельевна

generate_patronymic("Bacилий", "male") # Bacильевич
generate_patronymic("Bacилий", "female") # Bacильевна
```


