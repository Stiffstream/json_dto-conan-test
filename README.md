# json_dto-conan
Conan package for json_dto library

# How To Use

## Installing via Conan

To use json_dto via Conan the following steps are necessary:

1. Add the corresponding remote to your conan:

```bash
conan remote add stiffstream https://api.bintray.com/conan/stiffstream/public
```

2. Add json_dto to your `conanfile.txt`/`conanfile.py`:
```
[requires]
json-dto/0.2.8@stiffstream/stable
```

3. Install dependencies for your project:
```bash
conan install PROJECT_PATH --build=missing
```

## Adding json_dto to your CMakeLists.txt

One of the following approaches can be used:

```cmake
# 1. Find and add dependency.
find_package(json-dto CONFIG REQUIRED)
target_link_libraries(your_target json-dto::json-dto)

# 2. Setting up dependencies with Conan
target_link_libraries(your_target ${CONAN_LIBS})
```

# Feedback

If you have any questions about json_dto or its Conan package
feel free to ask us on `info@stiffstream.com`.
