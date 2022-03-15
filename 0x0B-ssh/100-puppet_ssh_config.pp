#!/usr/bin/env bash
# Set up ssh_config to reject password authentication

file_line { 'password auth':
	path  => '/etc/ssh/ssh_config',
	match => '^ PasswordAuthentication',
	line  => ' PasswordAuthentication no',
}

file_line { 'set identity file':
	path  => '/etc/ssh/ssh_config',
	match => '^ IdentityFile',
	line  => ' IdentityFile ~/.ssh/holberton',
}
