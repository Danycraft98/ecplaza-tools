# Generated by Django 3.2.3 on 2021-06-11 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='카테고리 ID')),
                ('name', models.CharField(max_length=100, verbose_name='카테고리')),
                ('date_entered', models.DateTimeField(auto_now=True, verbose_name='등록일')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='단어')),
                ('count', models.IntegerField(default=0, verbose_name='Word Count')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='static/uploads/', verbose_name='file')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('entered_date', models.DateTimeField(auto_now_add=True)),
                ('ca_id_extra', models.CharField(max_length=10, verbose_name='카테고리 ID')),
                ('it_id_extra', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('it_name', models.CharField(max_length=50, verbose_name='이름')),
                ('it_img_json', models.CharField(max_length=500, verbose_name='이미지 JSON')),
                ('it_origin', models.CharField(max_length=5, verbose_name='origin')),
                ('it_url', models.URLField(max_length=150, verbose_name='URL')),
                ('it_price', models.FloatField(verbose_name='Price')),
                ('it_whole_price', models.FloatField(verbose_name='Whole Price')),
            ],
        ),
        migrations.CreateModel(
            name='TourInfo',
            fields=[
                ('entered_date', models.DateTimeField(auto_now_add=True)),
                ('contentid', models.IntegerField(primary_key=True, serialize=False, verbose_name='컨텐트 ID')),
                ('contenttypeid', models.IntegerField(verbose_name='컨텐트 타입 ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('cat1', models.CharField(max_length=3, verbose_name='대분류 카테고리')),
                ('cat2', models.CharField(max_length=5, verbose_name='중분류 카테고리')),
                ('cat3', models.CharField(max_length=10, verbose_name='소분류 카테고리')),
                ('overview', models.TextField(blank=True, null=True, verbose_name='정보')),
                ('homepage', models.CharField(blank=True, max_length=200, null=True, verbose_name='홈페이지')),
                ('createdtime', models.BigIntegerField(blank=True, null=True, verbose_name='Created Time')),
                ('modifiedtime', models.BigIntegerField(blank=True, null=True, verbose_name='Modified Time')),
                ('firstimage', models.URLField(blank=True, max_length=150, null=True, verbose_name='First Image')),
                ('firstimage2', models.URLField(blank=True, max_length=150, null=True, verbose_name='Second Image')),
                ('readcount', models.IntegerField(blank=True, null=True, verbose_name='조회수')),
                ('telname', models.CharField(blank=True, max_length=50, null=True, verbose_name='전화번호 Name')),
                ('tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='전화번호')),
                ('addr1', models.CharField(blank=True, max_length=100, null=True, verbose_name='주소')),
                ('areacode', models.IntegerField(blank=True, null=True, verbose_name='Area Code')),
                ('sigungucode', models.IntegerField(blank=True, null=True, verbose_name='시군구 코드')),
                ('zipcode', models.IntegerField(blank=True, null=True, verbose_name='Zip 코드')),
                ('mapx', models.FloatField(blank=True, null=True, verbose_name='X Coordinate')),
                ('mapy', models.FloatField(blank=True, null=True, verbose_name='Y Coordinate')),
                ('mlevel', models.IntegerField(blank=True, null=True, verbose_name='M Level')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('tourinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tools.tourinfo')),
                ('eventstartdate', models.IntegerField(blank=True, null=True, verbose_name='시작 날짜')),
                ('eventenddate', models.IntegerField(blank=True, null=True, verbose_name='끝 날짜')),
            ],
            bases=('tools.tourinfo',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('tourinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tools.tourinfo')),
                ('lcnsno', models.BigIntegerField(blank=True, null=True, verbose_name='LSNS No.')),
                ('infocenterfood', models.CharField(blank=True, max_length=15, null=True, verbose_name='문의 전화번호')),
                ('chkcreditcardfood', models.CharField(blank=True, max_length=15, null=True, verbose_name='체크/신용카드')),
                ('discountinfofood', models.CharField(blank=True, max_length=15, null=True, verbose_name='할인 정보')),
                ('firstmenu', models.CharField(blank=True, max_length=30, null=True, verbose_name='메인 음식')),
                ('treatmenu', models.CharField(blank=True, max_length=30, null=True, verbose_name='사이드 음식')),
                ('kidsfacility', models.BooleanField(blank=True, default=False, null=True, verbose_name='아동시설')),
                ('parkingfood', models.CharField(blank=True, max_length=15, null=True, verbose_name='주차 가능')),
                ('opentimefood', models.CharField(blank=True, max_length=100, null=True, verbose_name='운영 시간')),
                ('restdatefood', models.CharField(blank=True, max_length=50, null=True, verbose_name='휴일 정보')),
            ],
            bases=('tools.tourinfo',),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=300, verbose_name='단어')),
                ('count', models.IntegerField(default=0, verbose_name='Word Count')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='tools.company', verbose_name='회사')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mall_type', models.CharField(max_length=30, verbose_name='Mall 타입')),
                ('mall_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='MALL 이름')),
                ('mall_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='MALL ID')),
                ('url', models.URLField(max_length=150, verbose_name='URL')),
                ('notes', models.TextField(blank=True, max_length=150, null=True, verbose_name='비고')),
                ('quantity', models.IntegerField(default=0, verbose_name='상품 갯수')),
                ('date_entered', models.DateTimeField(auto_now=True, verbose_name='등록일')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('date_download', models.DateTimeField(blank=True, null=True, verbose_name='다운로드 일')),
                ('date_apply', models.DateTimeField(blank=True, null=True, verbose_name='다운로드 일')),
                ('delete', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tools.category', verbose_name='카테고리')),
            ],
        ),
        migrations.CreateModel(
            name='DetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infoname', models.CharField(blank=True, max_length=100, null=True, verbose_name='정보 이름')),
                ('infotext', models.TextField(blank=True, null=True, verbose_name='정보 내용')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detailInfo', to='tools.tourinfo', verbose_name='아이템')),
            ],
        ),
        migrations.CreateModel(
            name='DetailImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originimgurl', models.URLField(blank=True, null=True, verbose_name='원본 Image')),
                ('smallimageurl', models.URLField(blank=True, null=True, verbose_name='Thumbnail Image')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detailImage', to='tools.tourinfo', verbose_name='아이템')),
            ],
        ),
    ]
