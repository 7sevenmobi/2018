
const PI = Math.PI;

const circleR = function (r){
    return PI * r * r;
};

const construct = function (){
    console.log('construct');
};

export {PI,circleR};

export default construct;

