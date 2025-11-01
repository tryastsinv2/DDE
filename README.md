# Проект для работы с данными о минералах

## Описание

Исследование, связанное с минералами. Данный репозиторий охватывает все основные этапы работы с данными.

## Ссылка на датасет
https://www.kaggle.com/datasets/lsind18/ima-database-of-mineral-properties

## Набор данных включает:
- название минерала
- его уникальную формулу (RRUFF и IMA) в виде обычного текста
- номер IMA и идентификаторы RUFF
- химические элементы
- страны, в которых он был обнаружен
- структурную группу
- возраст.

<table>
    <tr>
        <td>Название столбца</td>
        <td>Тип данных</td>
        <td>Пример значения</td>
        <td>Описание</td>
    </tr>
    <tr>
        <td>**Mineral Name**</td>
        <td>string</td>
        <td>"Abellaite"</td>
        <td>Название минерала</td>
    </tr>
    <tr>
        <td> **RRUFF Chemistry (plain)** </td>
        <td>string</td>
        <td>"NaPb2+2(CO3)2(OH)"</td>
        <td>Химическая формула в формате RRUFF</td>
    </tr>
    <tr>
        <td> **IMA Chemistry (plain)** </td>
        <td>string</td>
        <td>"NaPb2(CO3)2(OH)"</td>
        <td>Химическая формула в формате IMA (International Mineralogical Association)</td>
    </tr>
    <tr>
        <td> **Chemistry Elements** </td>
        <td>string</td>
        <td>"Na Pb C O H"</td>
        <td>Список химических элементов, входящих в состав минерала</td>
    </tr>
    <tr>
        <td>  **IMA Number**  </td>
        <td>string</td>
        <td>"IMA2014-111"</td>
        <td>Идентификационный номер IMA</td>
    </tr>
    <tr>
        <td>   **RRUFF IDs**   </td>
        <td>string</td>
        <td></td>
        <td>Идентификаторы в базе данных RRUFF</td>
    </tr>
    <tr>
        <td>   **Country of Type Locality**   </td>
        <td>string</td>
        <td>"Spain"</td>
        <td>Страна, где был впервые обнаружен минерал</td>
    </tr>
    <tr>
        <td>   **Year First Published**   </td>
        <td>integer</td>
        <td>2014</td>
        <td>Год первого опубликования описания минерала</td>
    </tr>
    <tr>
        <td>    **IMA Status**    </td>
        <td>string</td>
        <td>"Approved"</td>
        <td>Статус утверждения в IMA</td>
    </tr>
    <tr>
        <td>    **Structural Groupname**    </td>
        <td>string</td>
        <td>"Not in a structural group"</td>
        <td>Название структурной группы</td>
    </tr>
    <tr>
        <td>    **Fleischers Groupname**    </td>
        <td>string</td>
        <td></td>
        <td>Название группы по классификации Флейшера</td>
    </tr>
    <tr>
        <td>    **Status Notes**     </td>
        <td>string</td>
        <td>"Ibáñez-Insa J, Elvira J J, Llovet X, Pérez-Can..."</td>
        <td>Примечания и ссылки на публикации</td>
    </tr>
    <tr>
        <td>     **Crystal Systems**      </td>
        <td>string</td>
        <td>"hexagonal"</td>
        <td>Кристаллическая система</td>
    </tr>
    <tr>
        <td>     **Oldest Known Age (Ma)**       </td>
        <td>float</td>
        <td>370.0</td>
        <td>Самый древний известный возраст в миллионах лет</td>
    </tr>
</table>

## Установка
Через Shell
```bash
sudo apt update
curl -sSL https://install.python-poetry.org | python3 -
source ~/.bashrc
poetry install
```

Через Docker
```bash
docker build -t dde .
```

## Скриншот первых строчек датасета
<img width="1181" height="268" alt="DDE_скрин 10 колонок" src="https://github.com/user-attachments/assets/a33c3558-dc4a-4b69-9477-6a0c1c6106b9" />

## Визуализация
https://nbviewer.org/github/tryastsinv2/DDE/blob/main/notebooks/EDA.ipynb
