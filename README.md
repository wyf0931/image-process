# image-process
This is a simple image processor.

Feature list:

- Reset quality;
- Reset width;
- Reset hight;

## Quickstart
1. Install Python (3.10+);
2. Install dependencies: 
   ``` shell
   pip install -r requirements.txt
   ```
3. Start server: 
   ```shell
   sh run.sh
   ```
4. Open url in your browser: `http://127.0.0.1:8000`

## Preview

![web主页](./resource/web.png)

## Dependencies
- [Flask](https://github.com/pallets/flask)
- [Bootstrap V4.6](https://getbootstrap.com/)
- [gunicorn](https://github.com/benoitc/gunicorn)
- [Pillow](https://github.com/python-pillow/Pillow)