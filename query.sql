select category, count(category) from app group by category

select age_rating, count(age_rating) from app group by age_rating

select initial_date_of_release, app_size, app.app_name from app_publisher, app
where app_publisher.app_name = app.app_name
order by initial_date_of_release