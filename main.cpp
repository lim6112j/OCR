#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>
int main() {
    Pix *image;
    char *outText;
    char *configs[] ={"/Users/byeongcheollim/Documents/workspace/ocr/my.pattern.config"};
    int configs_size = 1;
    tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
    if(api->Init(NULL, "kor", tesseract::OEM_DEFAULT, configs, configs_size, NULL, NULL, false)) {
        fprintf(stderr, "Could not initialize tesseact.\n");
        exit(1);
    }
    api->SetPageSegMode(tesseract::PageSegMode::PSM_SINGLE_BLOCK);
    // image = pixRead("Arial.png");
    image = pixRead("/Users/byeongcheollim/Downloads/number4.png");
    api->SetImage(image);
    outText = api->GetUTF8Text();
    printf(outText);
    api->End();
    delete [] outText;
    pixDestroy(&image);
    return 0;
}