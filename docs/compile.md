# Compile the project

```bash
  pyinstaller -y -w --clean \
    --name pyui-livecompiler \
    --upx-exclude "Qt*.dll" \
    --add-data "src/presentation/resources;presentation/resources" \
    --icon=src/presentation/resources/images/logo.ico \
    src/program.py
```

```pwsh
  pyinstaller -y -w --clean `
    --name pyui-livecompiler `
    --upx-exclude "Qt*.dll" `
    --add-data "src/presentation/resources;presentation/resources" `
    --icon=src/presentation/resources/images/logo.ico `
    src/program.py
```
