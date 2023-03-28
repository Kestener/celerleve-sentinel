var dataset = ee.ImageCollection('JAXA/GPM_L3/GSMaP/v6/operational')
                  .filter(ee.Filter.date('2023-02-22', '2023-02-23'));
var precipitation = dataset.select('hourlyPrecipRate');
var precipitationVis = {
  min: 0.0,
  max: 30.0,
  palette:
      ['1621a2', 'ffffff', '03ffff', '13ff03', 'efff00', 'ffb103', 'ff2300'],
};
Map.setCenter(-45.6251126459802,-23.79208367859334);
Map.addLayer(precipitation, precipitationVis, 'Precipitation');