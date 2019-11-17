/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019-11-12 22:05:45                          */
/*==============================================================*/

SET character_set_server= utf8mb4;

drop table if exists classes_info;

drop table if exists course_info;

drop table if exists student_course;

drop table if exists student_info;

drop table if exists teacher_course;

drop table if exists teacher_info;

/*==============================================================*/
/* Table: classes_info                                          */
/*==============================================================*/
create table classes_info
(
   class_code           char(10) not null,
   tid                  char(10) not null,
   class_name           char(20) not null,
   class_grade          int not null,
   class_no             int not null,
   primary key (class_code)
);

/*==============================================================*/
/* Table: course_info                                           */
/*==============================================================*/
create table course_info
(
   cid                  char(20) not null,
   c_name               char(50) not null,
   introduce            char(255) not null,
   primary key (cid)
);

alter table course_info comment '所有课程的基本信息表';

/*==============================================================*/
/* Table: student_course                                        */
/*==============================================================*/
create table student_course
(
   cid                  char(20) not null,
   sid                  int not null,
   primary key (cid, sid)
);

/*==============================================================*/
/* Table: student_info                                          */
/*==============================================================*/
create table student_info
(
   sid                  int not null auto_increment,
   class_code           char(10),
   student_name         char(20) not null,
   s_sex                int not null,
   s_birthday           date not null,
   comments             char(255),
   primary key (sid)
);

alter table student_info comment '学生的基本信息';

/*==============================================================*/
/* Table: teacher_course                                        */
/*==============================================================*/
create table teacher_course
(
   tid                  char(10) not null,
   cid                  char(20) not null,
   primary key (tid, cid)
);

/*==============================================================*/
/* Table: teacher_info                                          */
/*==============================================================*/
create table teacher_info
(
   tid                  char(10) not null,
   class_code           char(10),
   t_name               char(20) not null,
   t_sex                int not null,
   t_birthday           date not null,
   in_charge            bool not null,
   primary key (tid)
);

alter table classes_info add constraint FK_teacher_class foreign key (tid)
      references teacher_info (tid) on delete restrict on update restrict;

alter table student_course add constraint FK_student_course foreign key (cid)
      references course_info (cid) on delete restrict on update restrict;

alter table student_course add constraint FK_student_course2 foreign key (sid)
      references student_info (sid) on delete restrict on update restrict;

alter table student_info add constraint FK_class_student foreign key (class_code)
      references classes_info (class_code) on delete restrict on update restrict;

alter table teacher_course add constraint FK_teacher_course foreign key (tid)
      references teacher_info (tid) on delete restrict on update restrict;

alter table teacher_course add constraint FK_teacher_course2 foreign key (cid)
      references course_info (cid) on delete restrict on update restrict;

alter table teacher_info add constraint FK_teacher_class2 foreign key (class_code)
      references classes_info (class_code) on delete restrict on update restrict;
