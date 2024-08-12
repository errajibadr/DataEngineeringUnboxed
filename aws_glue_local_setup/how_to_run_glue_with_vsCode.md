## HOW TO START A GLUE LOCAL SESSION IN VS CODE

For mac, command palet is `Cmd + shift + P`
For Windows, Command palet is `Ctrl + Maj + P`

### 0 - Set up AWS Credentials in ~/.aws

petit rappel :
`aws sts get-session-token`
pour obtenir des credentials temporaires. puis les coller sous [default] (le rajoute s'il n'y est pas) dans le fichier de creds.

cela devrait ressembler à:

```
[default]
AccessKeyId: ASIA...
SecretAccessKey:wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY
SessionToken: FQoGZXIvYXdz...
```

### 1 - Pull the glue image

```
 Docker Pull amazon/aws-glue-libs:glue_libs_4.0.0_image_01
```

### 2 - VS CODE Config

#### A - open workspace settings for you project or create one.

`Cmd + shift + P` , search & open "workspace settings (JSON)"

in this conf settings json, you should add :

```
"python.defaultInterpreterPath": "/usr/bin/python3",
"python.analysis.extraPaths": ["/home/glue_user/aws-glue-libs/PyGlue.zip:/home/glue_user/spark/python/lib/py4j-0.10.9-src.zip:/home/glue_user/spark/python/"]
```

the ExtraPAths we added above are the PYTHONPATHs the interpreter will look for source code and libraries used.

#### B - install Docker Container plugin for VS Code

Install plugin 'DevContainers' in VSCode to allow you connect to a docker image from VS.

once installed, to use it :
`Cmd + shift + P` , open "remote explorer" tab with a "focus on dev Containers".

You should see now all containers of you docker listed.

> WE ARE ALL SET !!

#### C - Run docker image

Run this commands in your terminal outside Vscode
don't forget to adapt your WORKSPACE_LOCATION to your project location

```shell
PROFILE_NAME=DEFAULT
WORKSPACE_LOCATION=~/repository/glue/
AWS_REGION = eu-west-1

docker run -it -v ~/.aws:/home/glue_user/.aws -v $WORKSPACE_LOCATION:/home/glue_user/workspace/ -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true -e AWS_REGION=$AWS_REGION --rm -p 4040:4040 -p 18080:18080 --name glue_pyspark amazon/aws-glue-libs:glue_libs_4.0.0_image_01 pyspark
```

#### D - Attach VSCODE To the container

Once done, go back to DevContainers tab and click "Attach to new window"

At last, choose /home/glue_user/workspace as defined in our run command when binding our WORKSPACE_LOCATION.

#### HAVE FUN !
