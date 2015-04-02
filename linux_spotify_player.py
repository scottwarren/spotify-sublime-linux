import sys
import os
import sublime

import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

from subprocess import Popen, PIPE

try:
  from Spotify.singleton import Singleton
except:
  from singleton import Singleton

# Wrap player interactions to compensate for different naming styles and platforms.
@Singleton
class SpotifyPlayer():
  def __init__(self):
    # dbus is for interacting between application (eg Sublime and Spotify)
    session_debus = debus.SessionBus()
    self.status_updater = None

    self.spotify = session_debus.get_object('org.mpris.MediaPlayer2.spotify')
    self.spotify = self.spotify.getProperties('/org/mpris/MediaPlayer2', 'org.freedesktop.DBus.Properties')
    self.spotify = self.spotify('/org/mpris/MediaPlayer2')

  def _execute_command(self, cmd):
    stdout = ""
    if cmd != "":
      bytes_cmd = cmd.encode('latin-1')
      p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
      stdout, stderr = p.communicate(bytes_cmd)

    return stdout.decode('utf-8').strip()

  def is_running(self):
    # res = self._execute_command('get running of application "Spotify"')
    return res == "true"

  def show_status_message(self):
    self.status_updater.run()

  def _get_state(self):
    # return self._execute_command('tell application "Spotify" to player state')

  def is_playing(self):
    return self._get_state() == "playing"

  def is_stopped(self):
    return self._get_state() == "stopped"

  def is_paused(self):
    return self._get_state() == "paused"

  # Current Track information
  def get_artist(self):
    # return self._execute_command('tell application "Spotify" to artist of current track')

  def get_album(self):
    # return self._execute_command('tell application "Spotify" to album of current track')

  def get_song(self):
    # return self._execute_command('tell application "Spotify" to name of current track')

  def get_position(self):
    # numstr = self._execute_command('tell application "Spotify" to player position')
    return int(float(numstr))

  def get_duration(self):
    # numstr = self._execute_command('tell application "Spotify" to duration of current track')
    return int(float(numstr))

  # Actions
  def play_pause(self):

  def play_track(self, track_url, attempts=0):

  def play(self, attempts=0):

  def pause(self):

  def next(self):

  def previous(self):

  def toggle_shuffle(self):

  def toggle_repeat(self):

