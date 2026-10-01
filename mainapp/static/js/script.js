var splide1 = new Splide( '#splide1', {
  type   : 'loop',
  perPage: 3,
  focus  : 'center',
  gap:10,
} );
splide1.mount();

var splide2 = new Splide( '#splide2', {
  type   : 'loop',
  perPage: 3,
  focus  : 'center',
  gap:0,
//   arrows: false
} );

splide2.mount();

var splide3 = new Splide( '#splide3', {
  direction: 'ttb',
  height   : '10rem',
  wheel    : true,
   arrows: false
} );

splide3.mount();