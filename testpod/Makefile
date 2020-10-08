REPOSITORY ?= testpod
VERSION    ?= 1.0


REGISTRY   ?= sureshkvl
IMAGE      ?= $(REGISTRY)/$(REPOSITORY):$(VERSION)

BUILD_OPTIONS = -t $(IMAGE)

default: build

build:
	docker build $(BUILD_OPTIONS) .
	docker tag $(IMAGE) $(REGISTRY)/$(REPOSITORY):latest

push:
	docker push $(IMAGE)
	docker push $(REGISTRY)/$(REPOSITORY):latest
