# Criar branch
usethis::pr_init(branch = "developer")

# Fazer push e abre pagina para fazer merge requeste
usethis::pr_push()

# voltar para a master, atualizar (pull) o conteúdo e deletar a branch criada
pr_finish()


