// rdservice.h
//
// Rivendell Services Manager
//
//   (C) Copyright 2018 Fred Gleason <fredg@paravelsystems.com>
//
//   This program is free software; you can redistribute it and/or modify
//   it under the terms of the GNU General Public License version 2 as
//   published by the Free Software Foundation.
//
//   This program is distributed in the hope that it will be useful,
//   but WITHOUT ANY WARRANTY; without even the implied warranty of
//   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//   GNU General Public License for more details.
//
//   You should have received a copy of the GNU General Public
//   License along with this program; if not, write to the Free Software
//   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
//

#ifndef RDSERVICE_H
#define RDSERVICE_H

#include <qmap.h>
#include <qobject.h>
#include <qprocess.h>
#include <qtimer.h>

#include "process.h"

#define RDSERVICE_CAED_ID 0
#define RDSERVICE_RIPCD_ID 1
#define RDSERVICE_RDCATCHD_ID 2
#define RDSERVICE_RDVAIRPLAYD_ID 3
#define RDSERVICE_RDREPLD_ID 4
#define RDSERVICE_LAST_ID 5
#define RDSERVICE_FIRST_DROPBOX_ID 100

class MainObject : public QObject
{
  Q_OBJECT;
 public:
  MainObject(QObject *parent=0);

 private slots:
  void processFinishedData(int id);
  void exitData();

 private:
  bool Startup(QString *err_msg);
  bool StartDropboxes(QString *err_msg);
  void KillProgram(const QString &program);
  void Shutdown();
  void ShutdownDropboxes();
  QMap<int,Process *> svc_processes;
  QTimer *svc_exit_timer;
};


#endif  // RDSERVICE_H