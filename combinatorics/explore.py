from utils import LETTERS
from utils import pretty_print


def n_permute_r(n, r):
    elements = LETTERS[:n]
    perm_evol_dict = {0: elements}

    def two_list_permutation(l1, l2):
        permutations = []

        for e1 in l1:
            for e2 in l2:
                if (e1 not in e2) and (e2 not in e1):
                    permutations.append(e1 + e2)
        return permutations

    pretty_print(n, 1, len(perm_evol_dict[0]), perm_evol_dict[0])

    for i in range(1, r):
        perm_evol_dict[i] = \
            two_list_permutation(perm_evol_dict[i - 1], elements)

        pretty_print(n, i + 1, len(perm_evol_dict[i]), perm_evol_dict[i])


def circular_n_permute_r(n, r):
    elements = LETTERS[:n]
    perm_evol_dict = {0: elements}

    def two_list_permutation(l1, l2):
        permutations = []


        return permutations

    pretty_print(n, 1, len(perm_evol_dict[0]), perm_evol_dict[0])

    for i in range(1, r):
        perm_evol_dict[i] = \
            two_list_permutation(perm_evol_dict[i - 1], elements)

        pretty_print(n, i + 1, len(perm_evol_dict[i]), perm_evol_dict[i])

if __name__ == "__main__":
    for j in range(3, 7):
        print("\n{0} element permutation".format(j))
        print("=====================")

        n_permute_r(j, j)