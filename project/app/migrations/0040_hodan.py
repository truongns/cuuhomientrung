# Generated by Django 3.1.2 on 2020-10-18 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20201019_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoDan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Hộ dân')),
                ('location', models.TextField(blank=True, default='', verbose_name='Địa chỉ')),
                ('status', models.IntegerField(choices=[(0, 'Chưa xác minh'), (1, 'Sẵn sàng'), (2, 'Không gọi được'), (3, 'Đang cứu hộ'), (4, 'Đang nghỉ')], default=0, verbose_name='Tình trạng')),
                ('phone', models.TextField(blank=True, default='', verbose_name='Điện thoại liên hệ')),
                ('note', models.TextField(blank=True, default='', verbose_name='Ghi chú')),
                ('cuuho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cuuho', verbose_name='Đơn vị cứu hộ tiếp cận')),
                ('huyen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.huyen')),
                ('thon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.thon')),
                ('tinh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tinh')),
                ('volunteer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tinhnguyenvien', verbose_name='Tình nguyện viên xác minh')),
                ('xa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.xa')),
            ],
        ),
    ]
