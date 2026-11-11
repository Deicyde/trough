---
declaration: section
origin: cited
lean: MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder, MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.mk, MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.lt, MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.irrefl, MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.trans, MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.total, MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.Profile, MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.SocialChoiceFunction
statement: formalized
proof: formalized
---

# Gibbard–Satterthwaite theorem

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html).

## Strict preference orders

## Strict preference orders for the Gibbard–Satterthwaite theorem

A strict total order on a
type $\alpha$ is a binary relation $<$ on $\alpha$ that is irreflexive ($a < a$ holds for no $a$),
transitive ($a < b$ and $b < c$ imply $a < c$) and total on distinct elements ($a \ne b$ implies
$a < b$ or $b < a$). In the Gibbard–Satterthwaite development it models a voter's strict
preference over alternatives.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#strict-total-order).

## Building a strict preference order in the Gibbard–Satterthwaite setting

A binary
relation $<$ on a type $\alpha$ that is irreflexive ($a < a$ holds for no $a$), transitive
($a < b$ and $b < c$ imply $a < c$) and total on distinct elements ($a \ne b$ implies $a < b$ or
$b < a$) defines a strict total order on $\alpha$ whose relation is $<$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.mk`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#mk).

## Relation of a strict preference order

The relation of a strict total order $T$ on a type
$\alpha$ is its underlying binary relation $\lt _T$ on $\alpha$, which is irreflexive, transitive,
and relates any two distinct elements in one direction or the other.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.lt`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#lt).

## Irreflexivity of strict preference

Let $T$ be a strict total order on a type $\alpha$,
with relation $\lt _T$. Then $a \lt _T a$ fails for every $a \in \alpha$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.irrefl`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#irrefl).

## Transitivity of strict preferences in the Gibbard–Satterthwaite setting

Let $<$ be the
relation of a strict total order on a type $\alpha$. If $a, b, c \in \alpha$ satisfy $a < b$ and
$b < c$, then $a < c$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.trans`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#trans).

## Strict preferences in the Gibbard–Satterthwaite setting are total

Let $<$ be the relation
of a strict total order on a type $\alpha$. If $a, b \in \alpha$ and $a \ne b$, then $a < b$ or
$b < a$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.StrictTotalOrder.total`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#total).

## Preference profiles for the Gibbard–Satterthwaite theorem

For a type $A$ of alternatives
and a type $V$ of voters, a profile is a function assigning to each voter $i \in V$ a strict total
order $\lt _i$ on $A$, the strict preference of voter $i$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.Profile`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#profile).

## Social choice functions

For a type $A$ of alternatives and a type $V$ of voters, a
resolute social choice function is a function $F$ sending each profile $p$ (an assignment of a
strict total order on $A$ to each voter in $V$) to a single chosen alternative $F(p) \in A$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.SocialChoiceFunction`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#social-choice-function).

## Top-ranked alternative

For a strict total order $o$ on the alternatives, write
$x \succ_o y$ when $x$ is related to $y$ by $o$ ($o$ ranks $x$ above $y$). An alternative $t$ is
top-ranked by $o$ when $t \succ_o b$ for every alternative $b \ne t$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.IsTopRanked`, a definition declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#is-top-ranked).

## Onto social choice function

A resolute social choice function $F$ is onto when every
alternative $a$ is chosen at some profile, that is, $F(p) = a$ for some profile $p$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.IsOnto`, a definition declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#is-onto).

## Profiles differing only at one voter

Let $p_1$ and $p_2$ be profiles, each assigning a
strict total order on the alternatives to every voter, and let $i$ be a voter. Then $p_2$ differs
from $p_1$ at most at voter $i$ when $p_1(j) = p_2(j)$ for every voter $j \ne i$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.DiffAtMostAt`, a definition declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#diff-at-most-at).

## Strategy-proof social choice function

For a strict total order $P$, write $x \succ_P y$
when $x$ is related to $y$ by $P$ ($P$ ranks $x$ above $y$). A resolute social choice function $F$
is strategy-proof when, for all profiles $p_1$, $p_2$ and every voter $i$ such that $p_1(j) =
p_2(j)$ for all voters $j \ne i$, it is not the case that $F(p_2) \succ_{p_1(i)} F(p_1)$: no voter
gains by misreporting alone, judged by the true order $p_1(i)$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.IsStrategyProof`, a definition declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#is-strategy-proof).

## Dictator of a social choice function

For a resolute social choice function $F$, a voter
$d$ is a dictator when, for every profile $p$, the chosen alternative $F(p)$ is top-ranked in the
preference order $p(d)$ of voter $d$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.IsDictator`, a definition declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#is-dictator).

## Dictatorial social choice function

A resolute social choice function $F$ is dictatorial
when some voter is a dictator for $F$: there is a voter $d$ such that, for every profile $p$, the
chosen alternative $F(p)$ is top-ranked in the preference order $p(d)$ of voter $d$.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.IsDictatorial`, a definition declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#is-dictatorial).

## Gibbard–Satterthwaite theorem, finiteness form

Let the set of alternatives be finite and the
set of voters be finite and nonempty, and suppose there are at least three distinct alternatives.
Then every resolute social choice function on profiles of strict preference orders that is onto
and strategy-proof is dictatorial.

## Sources

- A. Gibbard, Econometrica 41 (1973), 587-601, DOI 10.2307/1914083; M. A. Satterthwaite, J. Econom. Theory 10 (1975), 187-217, DOI 10.1016/0022-0531(75)90050-2.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.gibbard_satterthwaite_general`, a theorem declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 674](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#gibbard-satterthwaite-general).

## Gibbard–Satterthwaite theorem

Let the set of alternatives be finite and the set of voters be
finite and nonempty, and suppose there are at least three distinct alternatives. Then every
resolute social choice function on profiles of strict preference orders that is onto and
strategy-proof is dictatorial.

## Sources

- A. Gibbard, Econometrica 41 (1973), 587-601, DOI 10.2307/1914083; M. A. Satterthwaite, J. Econom. Theory 10 (1975), 187-217, DOI 10.1016/0022-0531(75)90050-2.

Formalized by `MathlibExt.GameTheory.SocialChoice.GibbardSatterthwaiteWanted.gibbard_satterthwaite`, a theorem declared in [MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/GibbardSatterthwaite.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html#gibbard-satterthwaite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gibbard–Satterthwaite theorem](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/social-choice/gibbard-satterthwaite-theorem)
