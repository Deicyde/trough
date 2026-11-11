---
declaration: section
origin: cited
lean: MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder, MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.mk, MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.lt, MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.irrefl, MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.trans, MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.total, MathlibExt.GameTheory.SocialChoice.ArrowWanted.Profile, MathlibExt.GameTheory.SocialChoice.ArrowWanted.SocialWelfareFunction
statement: formalized
proof: formalized
---

# Arrow's impossibility theorem

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html).

## Strict preference orders for Arrow's theorem

A strict total order on a type $\alpha$
consists of a relation $<$ on $\alpha$ that is irreflexive ($a < a$ holds for no $a$),
transitive ($a < b$ and $b < c$ imply $a < c$) and total on distinct elements ($a \ne b$
implies $a < b$ or $b < a$). Here it models a strict preference over alternatives.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#strict-total-order).

## Strict total order from a relation (Arrow's theorem)

A relation $<$ on a type $\alpha$
that is irreflexive ($a < a$ holds for no $a$), transitive ($a < b$ and $b < c$ imply $a < c$)
and total on distinct elements ($a \ne b$ implies $a < b$ or $b < a$) defines a strict total
order on $\alpha$.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.mk`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#mk).

## Preference relation of a strict total order (Arrow's theorem)

For a strict total order
$T$ on a type $\alpha$, this is its underlying binary relation $\lt _T$ on $\alpha$.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.lt`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#lt).

## Irreflexivity of strict preference (Arrow's theorem)

Let $T$ be a strict total order on a
type $\alpha$, and write $a \lt _T b$ for its relation. Then for every $a \in \alpha$, $a \lt _T a$ does
not hold.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.irrefl`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#irrefl).

## Strict preference orders for Arrow's theorem are transitive

If $<$ is a strict total order
on a type $\alpha$ and $a, b, c \in \alpha$ satisfy $a < b$ and $b < c$, then $a < c$.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.trans`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#trans).

## Strict preference orders for Arrow's theorem are total

If $<$ is a strict total order on
a type $\alpha$ and $a, b \in \alpha$ are distinct, then $a < b$ or $b < a$.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.StrictTotalOrder.total`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#total).

## Preference profile (Arrow's theorem)

A profile assigns to each voter a strict total
order on the alternatives.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.Profile`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#profile).

## Social welfare function

A social welfare function maps each unrestricted profile to a social strict total order.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.SocialWelfareFunction`, an abbreviation declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#social-welfare-function).

## Pareto condition

A social welfare function $F$ satisfies the Pareto condition if for
every profile $p$ and all alternatives $a, b$, whenever every voter strictly prefers $a$ to $b$ in
$p$, the social order $F(p)$ also strictly prefers $a$ to $b$.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.IsPareto`, a definition declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#is-pareto).

## Independence of irrelevant alternatives

A social welfare function $F$ satisfies
independence of irrelevant alternatives if for all profiles $p_1, p_2$ and all alternatives
$a, b$ the following holds: if every voter strictly prefers $a$ to $b$ in $p_1$ exactly when that
voter strictly prefers $a$ to $b$ in $p_2$, then $F(p_1)$ strictly prefers $a$ to $b$ exactly
when $F(p_2)$ does.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.IsIIA`, a definition declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#is-iia).

## Dictator of a social welfare function

A voter $d$ is a dictator for a social welfare
function $F$ if for every profile $p$ and all alternatives $a, b$, whenever $d$ strictly prefers
$a$ to $b$ in $p$, the social order $F(p)$ also strictly prefers $a$ to $b$.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.IsDictator`, a definition declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#is-dictator).

## Dictatorial social welfare function

A social welfare function $F$ is dictatorial if some
voter $d$ is a dictator for $F$: for every profile $p$ and all alternatives $a, b$, whenever $d$
strictly prefers $a$ to $b$ in $p$, the social order $F(p)$ also strictly prefers $a$ to $b$.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.IsDictatorial`, a definition declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#is-dictatorial).

## Arrow's impossibility theorem for strict preferences, general form

Suppose there are
finitely many alternatives, at least three of them, and finitely many voters, at least one. Then
every social welfare function, which assigns a strict total order of the alternatives to each
profile of strict total orders (one per voter), that satisfies the Pareto condition and
independence of irrelevant alternatives is dictatorial.

Here finiteness is assumed only as a property. The companion statement of Arrow's impossibility
theorem also fixes an explicit enumeration of the alternatives and of the voters and a decision
procedure for equality on each; this extra data does not change the mathematical content.

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.arrow_impossibility_general`, a theorem declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#arrow-impossibility-general).

## Arrow's impossibility theorem for strict preferences

Suppose there are finitely many
alternatives, at least three of them, and finitely many voters, at least one. Then every social
welfare function, which assigns a strict total order of the alternatives to each profile of strict
total orders (one per voter), that satisfies the Pareto condition and independence of irrelevant
alternatives is dictatorial.

## Sources

- K. J. Arrow, Social Choice and Individual Values, Wiley (1951; 2nd ed. 1963).

Formalized by `MathlibExt.GameTheory.SocialChoice.ArrowWanted.arrow_impossibility`, a theorem declared in [MathlibExt/GameTheory/SocialChoice/Arrow.lean, line 813](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/Arrow.lean#L813). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#arrow-impossibility).

## Arrow's impossibility theorem for weak preferences

Let $A$ be a type of alternatives
containing three distinct elements, and let $E$ be a finite nonempty set of voters. A profile
$P$ assigns to every voter $v$ a relation $P_v$ on $A$; it is admissible if, for every $v \in E$,
$P_v$ is a total preorder (reflexive, transitive, and $P_v(x, y)$ or $P_v(y, x)$ for all
$x, y \in A$). For a relation $R$ on $A$, say $R$ strictly ranks $a$ above $b$ if $R(a, b)$ holds
and $R(b, a)$ does not. Then there is no map $F$, sending each profile $P$ to a relation $F(P)$
on $A$, with all of the following properties. (Unrestricted domain) $F(P)$ is a total preorder
for every admissible $P$. (Pareto) For every admissible $P$ and all $a, b \in A$, if $P_v$
strictly ranks $a$ above $b$ for every $v \in E$, then $F(P)$ strictly ranks $a$ above $b$.
(Independence of irrelevant alternatives) For all admissible $P, Q$ and $a, b \in A$, if
$P_v(a, b) \iff Q_v(a, b)$ and $P_v(b, a) \iff Q_v(b, a)$ for every $v \in E$, then
$F(P)(a, b) \iff F(Q)(a, b)$ and $F(P)(b, a) \iff F(Q)(b, a)$. (Non-dictatorship) For every
$d \in E$ there are an admissible $P$ and $a, b \in A$ such that $P_d$ strictly ranks $a$ above
$b$ but $F(P)$ does not.

## Sources

- https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem.

Formalized by `MetaMathlibExt.arrowImpossibility`, a theorem declared in [MathlibExt/GameTheory/SocialChoice/ArrowImpossibility.lean, line 793](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SocialChoice/ArrowImpossibility.lean#L793). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html#arrow-impossibility-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arrow's impossibility theorem](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/social-choice/arrow-s-impossibility-theorem)
