import {
  Module,
} from '@nestjs/common';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsersModule } from './App/users/users.module';
import { CategoriesModule } from 'src/App/categories/categories.module';
import { APP_FILTER, APP_INTERCEPTOR } from '@nestjs/core';
import { AuthModule } from './App/auth/auth.module';
import { MulterModule } from '@nestjs/platform-express';
import { ConfigModule } from '@nestjs/config';
import { TypeOrmConfigService } from 'src/config/typeorm.config';
import { HttpErorFilter } from 'src/shared/http-exception.filter';
import { LoggingInterceptor } from './interceptors/logging.interceptor';
import { TransformInterceptor } from './interceptors/TransformInterceptor';
import { PermissionModule } from './App/permission/permission.module';
import { JobsModule } from './App/jobs/jobs.module';
import { AddressModule } from './App/address/address.module';
import { ApplyController } from './App/apply/apply.controller';
import { UploadModule } from './App/upload/upload/upload.module';
import { ServeStaticModule } from '@nestjs/serve-static';
import { TagsModule } from './App/tags/tags.module';
import { NotificationModule } from './App/notification/notification.module';

@Module({
  imports: [
    ServeStaticModule.forRoot(),
    ConfigModule.forRoot(),
    UsersModule,
    CategoriesModule,
    UploadModule,
    PermissionModule,
    AuthModule,
    AddressModule,
    TagsModule,
    JobsModule,
    NotificationModule,
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      useClass: TypeOrmConfigService,
    }),
    MulterModule.register({
      dest: './uploads',
    }),
  ],
  controllers: [ApplyController],
  providers: [
    {
      provide: APP_FILTER,
      useClass: HttpErorFilter,
    },
    {
      provide: APP_INTERCEPTOR,
      useClass: LoggingInterceptor,
    },
    {
      provide: APP_INTERCEPTOR,
      useClass: TransformInterceptor,
    },
    AppService,
  ],
})
export class AppModule {
}
