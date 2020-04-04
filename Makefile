build-test-image:
	docker build --no-cache -t test-app -f docker/test.Dockerfile .

run-tests: build-test-image
	docker run --rm test-app