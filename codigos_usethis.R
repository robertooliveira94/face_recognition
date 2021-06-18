# https://beatrizmilz.github.io/RLadies-Git-RStudio-2019/#1

# Criar branch
usethis::pr_init(branch = "developer")

# Fazer commit no quadro

# Fazer push e abre pagina para fazer merge requeste
usethis::pr_push()

# voltar para a master, atualizar (pull) o conteúdo e deletar a branch criada
pr_finish()


