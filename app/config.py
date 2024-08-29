# Este archivo configura la app

# Configura la cadena de conexión desde el panel de Vercel
#SQLALCHEMY_DATABASE_URI = "postgres://default:ARgfMHVes85Z@ep-white-morning-a40680zk.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
SQLALCHEMY_DATABASE_URI = "postgresql://default:ARgfMHVes85Z@ep-white-morning-a40680zk.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

#stackoverflow hace 4M: dice que la URI debe comenzar con postgresql ya que no acepta postgres (antes si lo aceptaba)
