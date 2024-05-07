const decodeImage = require("jimp").read;
const qrcodeReader = require("qrcode-reader");
function qrDecode(data, callback) {
    const time = sd.format(new Date(), 'YYYY-MM-DD HH:mm:ss');
    console.log(time)
    decodeImage(data, function (err, image) {
        if (err) {
            callback(false);
            return;
        }
        let decodeQR = new qrcodeReader();
        decodeQR.callback = function (errorWhenDecodeQR, result) {
            if (errorWhenDecodeQR) {
                callback(false);
                return;
            }
            if (!result) {
                callback(false);
                return;
            } else {
                const time = sd.format(new Date(), 'YYYY-MM-DD HH:mm:ss');
                console.log(time)
                callback(result.result);
            }
        };
        decodeQR.decode(image.bitmap);
    });
}

