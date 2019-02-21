function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample

  var url = `/metadata/${sample}`;
  d3.json(url).then(function(metadata) {
    // Use d3 to select the panel with id of `#sample-metadata`
    var sample_metadata=d3.select(`#sample-metadata`)
    // Use `.html("") to clear any existing metadata
    sample_metadata.html("")
    // Use `Object.entries` to add each key and value pair to the panel
    Object.entries(metadata).forEach(function([item]) {
      sample_metadata
            .text(item);
     });
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var url = `/samples/${sample}`;
  d3.json(url).then(function(response) {

    console.log(response);

    var value = response.sample_values;
    var otu_ids = response.otu_ids;
    var otu_labels = response.otu_labels;


    // @TODO: Build a Bubble Chart using the sample data

    var trace1 = {
      x: otu_ids,
      y: value,
      mode: 'markers',
      type: "scatter",
      marker: {
        size: value
        //color:[]
        // text value??
      }
    };

    var data = [trace1];

    var layout = {
    title: 'Marker Size',
    showlegend: false,
    height: 600,
    width: 600
    };

Plotly.newPlot("bubble", data, layout);

    // @TODO: Build a Pie Chart

    var data = [{
      values: value.slice(0,9),
      labels: otu_ids.slice(0,9),
      type: "pie"
    }];
  
    var layout = {
      height: 600,
      width: 800
    };
  
    Plotly.plot("pie", data, layout);
  }
  
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
};

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
};

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
};

// Initialize the dashboard
init();


