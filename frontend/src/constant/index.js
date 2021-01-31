import NumberFormat from 'react-number-format'
export  const columns = {
    encimeras : [
      {
        name: 'MATERIAL',
        selector: 'MATERIAL',
        sortable: true
      },
      {
        name: 'COLOR',
        selector: 'COLOR',
        sortable: true
      },
      {
        name: 'ACABADO',
        selector: 'ACABADO',
        sortable: true
        },
      {
        name: 'GROSOR',
        selector: 'GROSOR',
        sortable: true
      },
      {
        name: 'MEDIDA',
        selector: 'MEDIDA',
        sortable: true
      },
      {
        name: 'PRECIO_METRO',
        selector: 'PRECIO_METRO',
        sortable: true,
        right: true,
        cell: row => (new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(row.PRECIO_METRO))

      },
      {
        name: 'TOTAL',
        selector: 'TOTAL',
        sortable: true,
        right: true,
        cell: row => (new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(row.TOTAL))
      }
    ],
    inventario : [
      {
        name: 'MATERIAL',
        selector: 'MATERIAL',
        sortable: true
      },
      {
        name: 'COLOR',
        selector: 'COLOR',
        sortable: true
      },
      {
        name: 'ACABADO',
        selector: 'ACABADO',
        sortable: true
        },
      {
        name: 'GROSOR',
        selector: 'GROSOR',
        sortable: true
      },
      {
        name: 'MEDIDA',
        selector: 'MEDIDA',
        sortable: true
      },
      {
        name: 'PRECIO_M2',
        selector: 'PRECIO_M2',
        sortable: true,
        right: true,
        cell: row => (new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(row.PRECIO_M2))

      },
      {
        name: 'TOTAL',
        selector: 'TOTAL',
        sortable: true,
        right: true,
        cell: row => (new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(row.TOTAL))

      }  
  ],
    fregaderos : [
      {
        name: 'MATERIAL',
        selector: 'MATERIAL',
        sortable: true
      },
      {
        name: 'COLOR',
        selector: 'COLOR',
        sortable: true
      },
      {
        name: 'MEDIDA',
        selector: 'MEDIDA',
        sortable: true
      },
      {
        name: 'TOTAL',
        selector: 'TOTAL',
        sortable: true,
        right: true,
        cell: row => (new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(row.TOTAL))
      }
    ],
    suplementos : [
      {
        name: 'CONCEPTO',
        selector: 'CONCEPTO',
        sortable: true
      },
      {
        name: 'CANTIDAD',
        selector: 'CANTIDAD',
        sortable: true
      },
      {
        name: 'PRECIO_UNIDAD',
        selector: 'PRECIO_UNIDAD',
        sortable: true,
        right: true,
        cell: row => (new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(row.PRECIO_UNIDAD))

      },
      {
        name: 'TOTAL',
        selector: 'TOTAL',
        sortable: true,
        right: true,
        cell: row => (new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(row.TOTAL))

      }
    ],
  };
  
  
    export const URL_FILTER_DATA = 'http://localhost:8000/filter_data';
    export const URL_CREATE_DATA_INICIAL = 'http://localhost:8000/create_data_inicial';