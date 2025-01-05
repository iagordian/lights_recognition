
run_app:
	poetry run python3 -m scripts.kill_port
	poetry run uvicorn app.api:app --reload --port=5000 --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"
	

recreate_db:
	poetry run python3 -m scripts.recreate_db

save_demo_videos_to_json:
	poetry run python3 -m scripts.save_demo_videos_to_json

clear_images_sample:
	poetry run python3 -m scripts.clear_images_sample

unpack_archives:
	poetry run python3 -m scripts.unpack_archives

test_model_learn:
	poetry run python3 -m scripts.test_model_learn

test_model_learn_continue:
	poetry run python3 -m scripts.test_model_learn_continue

model_learn:
	poetry run python3 -m scripts.model_learn

model_learn_continue:
	poetry run python3 -m scripts.model_learn_continue

move_model_state_file:
	poetry run python3 -m scripts.move_model_state_file

test_actual_model:
	poetry run python3 -m scripts.test_actual_model

clear_tests_outputs:
	poetry run python3 -m scripts.clear_tests_outputs