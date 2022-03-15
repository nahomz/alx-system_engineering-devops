# 0x0B. SSH
This directory covers SSH operations and configurations.

## Files
### [0-use_a_private_key](./0-use_a_private_key)
A Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:
	Only use ssh single-character flags
        You cannot use -l
	You do not need to handle the case of a private key protected by a passphrase

### [1-create_ssh_key_pair](./1-create_ssh_key_pair)
Bash script that creates an RSA key pair.


### [2-ssh_config](./2-ssh_config)
SSH client configuration file for connecting to a server without typing a password.

### [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp)
Let's practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password

	
