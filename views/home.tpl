<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="/_static/bootstrap/assets/ico/favicon.png">

    <title>{{project}}</title>

    <!-- Bootstrap core CSS -->
    <link href="/_static/bootstrap/dist/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/_static/jumbotron.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="/_static/bootstrap/assets/js/html5shiv.js"></script>
      <script src="/_static/bootstrap/assets/js/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">{{project}}</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
            <!--
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li>
            -->
          </ul>
          <!--
          <form class="navbar-form navbar-right">
            <div class="form-group">
              <input type="text" placeholder="Email" class="form-control">
            </div>
            <div class="form-group">
              <input type="password" placeholder="Password" class="form-control">
            </div>
            <button type="submit" class="btn btn-success">Sign in</button>
          </form>
          -->
        </div><!--/.navbar-collapse -->
      </div>
    </div>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1>Hello, LDAP user!</h1>
        <p>A simple management tool for LDAP server.</p>
        <p><a class="btn btn-primary btn-lg">Learn more &raquo;</a></p>
      </div>
    </div>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-lg-6">
          % if alert:
          <div class="{{alert_type}} alert-dismissable">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            <strong>{{alert_title}}</strong> {{alert_message}}
          </div>
          % end
          <h2>Password Utils</h2>
            <form class="form-horizontal" role="form" action="/" method="post" accept-charset="utf-8">
              <div class="form-group">
                <label for="inputUsername" class="col-lg-3 control-label">Username</label>
                <div class="col-lg-6">
                  <input type="text" class="form-control" name="inputUsername" id="inputUsername" placeholder="Username">
                </div>
              </div>
              <div class="form-group">
                <label for="inputOldPassword" class="col-lg-3 control-label">Old password</label>
                <div class="col-lg-6">
                  <input type="password" class="form-control" name="inputOldPassword" id="inputOldPassword" placeholder="Current password">
                </div>
              </div>
              <div class="form-group">
                <label for="inputNewPassword" class="col-lg-3 control-label">New password</label>
                <div class="col-lg-6">
                  <input type="password" class="form-control" name="inputNewPassword" id="inputNewPassword" placeholder="Desire password">
                </div>
              </div>
              <div class="form-group">
                <div class="col-lg-offset-3 col-lg-10">
                  <button type="submit" class="btn btn-default">Modify</button>
                </div>
              </div>
            </form>
        </div>
        <div class="col-lg-6">
          <h2>Recent Users</h2>
          <table class="table">
              <tr><th>RDN</th><th>DN</th></tr>
              % for user in users:
              <tr><td>{{user["rdn"]}}</td><td>{{user["dn"]}}</td></tr>
              % end 
          </table>
       </div>
      </div>

      <hr>

      <footer>
        <p>&copy; {{project}} 2013</p>
      </footer>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/_static/bootstrap/assets/js/jquery.js"></script>
    <script src="/_static/bootstrap/dist/js/bootstrap.min.js"></script>
  </body>
</html>
