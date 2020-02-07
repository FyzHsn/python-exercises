from utils import LETTERS
from utils import pretty_print


def two_list_permutation(l1, l2, circular=False):
    permutations = []
    all_non_circular_permutations = []

    for e1 in l1:
        for e2 in l2:
            if (e1 not in e2) and (e2 not in e1):
                permutation = e1 + e2

                if (circular and permutation not in
                        all_non_circular_permutations) or not circular:
                    permutations.append(permutation)

                all_non_circular_permutations += \
                    circular_variations(permutation)

    return permutations


def circular_variations(permutation):
    variations = [permutation]

    for i in range(1, len(permutation)):
        variations.append(variations[i - 1][-1] + variations[i - 1][0:-1])

    return variations


def n_permute_r(n, r, circular=False):
    elements = LETTERS[:n]
    perm_evol_dict = {0: elements}

    pretty_print(n, 1, len(perm_evol_dict[0]), perm_evol_dict[0])

    for i in range(1, r):
        perm_evol_dict[i] = \
            two_list_permutation(perm_evol_dict[i - 1], elements,
                                 circular=circular)

        pretty_print(n, i + 1, len(perm_evol_dict[i]), perm_evol_dict[i])


if __name__ == "__main__":
    for j in range(3, 8):
        print("\n{0} element permutation".format(j))
        print("=====================")

        n_permute_r(j, j, True)
        