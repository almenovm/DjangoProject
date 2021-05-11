USER_ROLE_SUPER_USER = 1
USER_ROLE_CUSTOMER = 2

USER_ROLES = (
    (USER_ROLE_SUPER_USER, 'super admin'),
    (USER_ROLE_CUSTOMER, 'customer'),
)


M_TYPE_CHOICES = (
    ('Еженедельник', 'Еженедельник'),
    ('Ежемесячник', 'Ежемесячник')
)

R_TYPE_CHOICES = (
    ('Для детей', 'Для детей'),
    ('18+', '18+'),
    ('16+', '16+')
)

COLOR_CHOICES = (
    ('Черно-белый', 'Черно-белый'),
    ('Цветной', 'Цветной')
)

RATING_CHOICES = (
    ('0/5 - оценок пока нет', '0/5 - оценок пока нет'),
    ('1/5', '1/5'),
    ('2/5', '2/5'),
    ('3/5', '3/5'),
    ('4/5', '4/5'),
    ('5/5', '5/5'),
)