# P2P Orders Analytics

Небольшой скрипт для анализа оборота и прибыли.

Работает с Байбит и Хуоби, возможно позже добавлю Бинанс.

## Зависимости

Для работы скрипта понадобится Питон, я использовал версию 3.11

Скрипту не нужен интернет, нужно скачать свои сделки в формате `.xlsx` с Хуоби или Байбит.

## Установка

Скачай проект

```bash
  git clone https://github.com/aquarell-dev/p2p-orders-analytics.git
```

Перейди в директорию со скриптом

```bash
  cd p2p-orders-analytics
```

Установи зависимости

```bash
  pip install -r requirements.txt
```

## Запуск

Нужно скачать свои сделки с Байбита и(или) Хуоби и поместить их в папку `files`

Файлы должны называться `bybit.xlsx` и `huobi.xls` соотвественно

Запуск скрипта с выводом в консоль

```bash
python main.py ###
```

Запуск скрипта с выводом в файл `output.xlsx`

```bash
python main.py -o output.xlsx
```

Запуск скрипта только для хуоби

```bash
python main.py huobi -o output.xlsx
```

Запуск скрипта только для байбит

```bash
python main.py bybit -o output.xlsx
```
