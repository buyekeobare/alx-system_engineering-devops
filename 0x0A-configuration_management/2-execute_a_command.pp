# creates a manifest that kills the process with the name killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
