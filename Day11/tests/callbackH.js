getData(function(a) {
    getMoreData(a, function(b) {
      getMoreData(b, function(c) {
        getMoreData(c, function(d) {
          getMoreData(d, function(e) {
            // Do something with the data
            console.log(e);
          });
        });
      });
    });
  });