#include <stdio.h>
#include <stdlib.h>


struct hucre{
    int icerik;
    struct hucre *sonraki;
};

struct hucre* hucre_olustur(int icerik){
    struct hucre *a;
    a=(struct hucre*)malloc(sizeof(struct hucre));
    if(a==NULL){
        printf("Heap alaninda yer ayrilamadi ...\n");
        exit(1);
    }
    a->icerik=icerik;
    a->sonraki=NULL;
}

void liste_sonuna_ekle(int icerik,struct hucre **liste_basi){
    struct hucre* a=hucre_olustur(icerik);
    if(*liste_basi==NULL){
        a->sonraki=*liste_basi;
        *liste_basi=a;
    }
    else {
        struct hucre *x=*liste_basi;
        while(x->sonraki!=NULL){
            x=x->sonraki;
        }
        x->sonraki=a;
    }
}

void liste_yaz(struct hucre *liste_basi){
    while(liste_basi!=NULL){
        printf("%4d ",liste_basi->icerik);
        liste_basi=liste_basi->sonraki;
    }
    printf("\n");
}



void liste_eleman_sil(int silinen, struct hucre **liste_basi){
    struct hucre *temp=*liste_basi;
    struct hucre *once;
   
    while(temp!=NULL && temp->icerik!=silinen){
        once = temp;
        temp=temp->sonraki;
    }
    if(temp==NULL) return;
    else {
        if(temp==*liste_basi) *liste_basi=(*liste_basi)->sonraki;
        else once->sonraki=temp->sonraki;
        free(temp);
    }
       
   }
void liste_sirala(struct hucre **liste_basi){
    struct hucre *a,*b,*c,*d;
   
    if(*liste_basi == NULL || (*liste_basi)->sonraki==NULL) return;
   
    d=(*liste_basi)->sonraki;
    (*liste_basi)->sonraki=NULL;
   
    while(d!=NULL){
        c=d;
        d=d->sonraki;
        b=*liste_basi;
        while(b!=NULL && b->icerik < c->icerik){
            a=b;
            b=b->sonraki;
        }
        if(b==*liste_basi){
            c->sonraki=*liste_basi;
            *liste_basi=c;
        }
        else {
            a->sonraki = c;
            c->sonraki = b;
        }
        }
    }


int main(int argc, char** argv) {
  
    struct hucre *liste1=NULL;
   
     liste_sonuna_ekle(10,&liste1);
     liste_sonuna_ekle(15,&liste1);
     liste_sonuna_ekle(50,&liste1);
     liste_sonuna_ekle(1,&liste1);
     liste_yaz(liste1);
 
    
     liste_eleman_sil(15,&liste1);
     liste_yaz(liste1);
 
    return 0;
}
