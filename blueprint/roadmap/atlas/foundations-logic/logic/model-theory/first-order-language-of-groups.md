---
declaration: section
origin: cited
lean: FirstOrder.Language.GroupFunction, FirstOrder.Language.groupLanguage, FirstOrder.Language.groupLanguageStructure, FirstOrder.Language.groupLanguage_functions, FirstOrder.Language.groupLanguage_relations, FirstOrder.Language.groupLanguageStructure_mul, FirstOrder.Language.groupLanguageStructure_inv, FirstOrder.Language.groupLanguageStructure_one
statement: formalized
proof: formalized
---

# First-order language of groups

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html).

## Group function symbols

The function symbols of the first-order language of groups,
graded by arity, are a constant symbol for the identity (arity $0$), a symbol for inversion
(arity $1$) and a symbol for multiplication (arity $2$); there are no others.

Formalized by `FirstOrder.Language.GroupFunction`, an inductive type declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-function).

## The first-order language of groups

The first-order language of groups has the group
function symbols (a constant for the identity, a unary symbol for inversion and a binary symbol
for multiplication) as its function symbols and no relation symbols.

Formalized by `FirstOrder.Language.groupLanguage`, a definition declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-language).

## The canonical structure on a group

For a group $G$, the canonical structure on $G$ for
the first-order language of groups interprets the identity constant as the identity $1$ of $G$,
inversion as $x \mapsto x^{-1}$ and multiplication as $(x, y) \mapsto xy$; there are no
relation symbols to interpret.

Formalized by `FirstOrder.Language.groupLanguageStructure`, a definition declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-language-structure).

## The function symbols of the language of groups

For every $n \in \mathbb{N}$, the
$n$-ary function symbols of the first-order language of groups are exactly the group function
symbols of arity $n$.

Formalized by `FirstOrder.Language.groupLanguage_functions`, a theorem declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-language-functions).

## The language of groups has no relation symbols

For every $n \in \mathbb{N}$, the
first-order language of groups has no $n$-ary relation symbols.

Formalized by `FirstOrder.Language.groupLanguage_relations`, a theorem declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-language-relations).

## Multiplication in the canonical structure

For every group $G$ and every pair
$(x_0, x_1)$ of elements of $G$, the multiplication symbol of the language of groups,
interpreted in the canonical structure on $G$, sends $(x_0, x_1)$ to $x_0 x_1$.

Formalized by `FirstOrder.Language.groupLanguageStructure_mul`, a theorem declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-language-structure-mul).

## Inversion in the canonical structure

For every group $G$ and every one-element tuple
$(x_0)$ of elements of $G$, the inversion symbol of the language of groups, interpreted in the
canonical structure on $G$, sends $(x_0)$ to $x_0^{-1}$.

Formalized by `FirstOrder.Language.groupLanguageStructure_inv`, a theorem declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-language-structure-inv).

## The identity in the canonical structure

For every group $G$, the identity constant
symbol of the language of groups, interpreted in the canonical structure on $G$, takes the value
$1$ at the empty tuple, where $1$ is the identity of $G$.

Formalized by `FirstOrder.Language.groupLanguageStructure_one`, a theorem declared in [MathlibExt/ModelTheory/GroupLanguage.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/ModelTheory/GroupLanguage.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html#group-language-structure-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: First-order language of groups](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/first-order-language-of-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/model-theory/first-order-language-of-groups)
