#include<iostream>
#include<cmath>
using namespace std;


double x[99]={1,2,3,4,5,6,7,8,9,10}, y[99]={7,9,14,14,21,24,23,29,30,34};
int l=5;

void menampil()	
	{int q; cout<<"Masukkan Jumlah Kolom Yang Ingin Ditampilkan\t:"; cin>>q;cout<<endl;
	cout<<"No."<<"\t"<<"X[i]"<<"\t\t"<<"Y[i]"<<endl;
	for (int i=0;i<q;i++)
	{cout<<i+1<<".\t"<<x[i]<<"\t\t"<<y[i]<<endl;}
	}
void ubahan(int n)
	{cout<<"Nomor data yang ingin anda ubah\t:"; cin>>n;
	{cout<<"X Ke-"<<n<<"\t:";cin>>x[n-1];cout<<"Y Ke-"<<n<<"\t:";cin>>y[n-1];}
}
	
void menambah()
{	l=l+1;
	cin>>x[l-1];cin>>y[l-1];}
	
void hitung(int n=5)
	{{double k=0, l=0, m=0, r2, dev, X=0, Y=0, P=0, Q=0, a, b, jum;
	for (int i=0;i<n;i++)
	{X+=x[i]; Y+=y[i]; P+=pow(x[i],2); Q+=(x[i]*y[i]);}
	a=(Q*n-Y*X)/(P*n-X*X);b=(Y*P-X*Q)/(P*n-X*X);
	jum=Y/n;
	for (int i=0;i<n;i++)
	{k+=pow((a*x[i]+b-jum),2);
	l+=pow((y[i]-jum),2);
	m+=pow((y[i]-(a*x[i]+b)),2);}
	r2=k/l;dev=sqrt(m/(n-1));
	cout<<"Nilai a ="<<a<<"\n";cout<<"Nilai b ="<<b<<"\n";
	cout<<"Faktor korelasi ="<<r2<<"\n";cout<<"Deviasi standar ="<<dev<<"\n";}}
	

int main(){

	{cout<<"Analisis Regresi Linier\n---------------------------\n";
	cout<<"Kelompok\n---------------------------\n";
char menu[5][100]={"Tampilan Data Kolom X Dan Y","Ubah Data Yang Ada","Tambah Data Yang Ada","Tampilkan hasil perhitungan","Selesai"};
int pilihan;
	do{for(int i=0;i<5;i++) {cout<<i+1<<". "<<menu[i]<<"\n";}
	cout<<"Inputkan nomor pilihan anda : ";cin>>pilihan;
switch (pilihan)
	{case 1 : {cout<<"\n";menampil();cout<<"\n";break;}
	case 2 : {cout<<"\n";ubahan(5);cout<<"\n";break;}
	case 3 : {cout<<"\n";menambah();cout<<"\n";break;}
	case 4 : {cout<<"\n";hitung(5);cout<<"\n";break;}
	case 5 : {cout<<"\nTerima kasih\n\n";break;}
	default : {cout<<"\nAnda salah pilih\n\n";}}
	}
	
	while(pilihan!=5);
	system("pause");
	return 0;
	
}}
