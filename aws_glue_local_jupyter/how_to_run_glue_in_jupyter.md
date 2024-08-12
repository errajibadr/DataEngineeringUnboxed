## HOW TO START A Jupyter Server for Glue/Pyspark

in VsCode:
For mac, command palet is `Cmd + shift + P`
For Windows, Command palet is `Ctrl + Maj + P`,

Tip : install Markdown Command Runner Plugin, so you can directly run this commands in your terminal

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

```shell
 Docker Pull amazon/aws-glue-libs:glue_libs_4.0.0_image_01
```

### 2 - Run Jupyter Server in Docker

Run this commands in your terminal outside Vscode
don't forget to adapt your JUPYTER_WORKSPACE_LOCATION to your jupyter workspace location

```shell
PROFILE_NAME=DEFAULT
JUPYTER_WORKSPACE_LOCATION=~/repository/glue/local_glue_jupyter/
AWS_REGION=eu-west-1
PYTHONPATH=/opt/project/

docker run -it --memory=8g -v ~/.aws:/home/glue_user/.aws -v $JUPYTER_WORKSPACE_LOCATION:/home/glue_user/workspace/jupyter_workspace/ -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true -e AWS_REGION=$AWS_REGION --rm -p 4040:4040 -p 18080:18080 -p 8998:8998 -p 8888:8888 --name glue_jupyter_lab amazon/aws-glue-libs:glue_libs_4.0.0_image_01 /home/glue_user/jupyter/jupyter_start.sh
```

nb: if you want to add your project to source code accessible from your notebook;
you can add `-v $PROJECT_LOCATION:$PYTHONPATH` to mount your project in the container at $PYTHONPATH location
Then add ` -e PYTHONPATH=$PYTHONPATH` to inform the interpreter that he will find source code there.

#### 3 - Use your notebook

Once running, you can

- start using notebook directly from http://127.0.0.1:8888/lab/ in your favorite web browser.

- you can leverage VScode to use notebook.

for the latter, open your notebook and choose

> "select Kernel" in top right.
> Existing Server
> http://127.0.0.1:8888/lab
> Pyspark

#### HAVE FUN !
