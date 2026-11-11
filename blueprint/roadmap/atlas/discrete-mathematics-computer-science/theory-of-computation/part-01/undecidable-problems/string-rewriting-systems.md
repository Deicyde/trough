---
declaration: section
origin: cited
lean: Cslib.Decidability.Rewriting.Rule, Cslib.Decidability.Rewriting.Step, Cslib.Decidability.Rewriting.Derives, Cslib.Decidability.Rewriting.SR, Cslib.Decidability.Rewriting.NonemptyRules, Cslib.Decidability.Rewriting.lift, Cslib.Decidability.Rewriting.startCard, Cslib.Decidability.Rewriting.finalCard
statement: formalized
proof: formalized
---

# String rewriting systems

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html).

## Rewriting rules

A rewriting rule over an alphabet $\alpha$ is a pair $(l, r)$ of words
over $\alpha$; applying it replaces an occurrence of $l$ by $r$.

Formalized by `Cslib.Decidability.Rewriting.Rule`, an abbreviation declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#rule).

## One-step rewriting

Let $R$ be a string rewriting system, given as a list of rules. A word
$w$ rewrites to a word $w'$ in one step of $R$ when there are a rule $(l, r)$ of $R$ and words
$u$ and $v$ with $w = u l v$ and $w' = u r v$.

Formalized by `Cslib.Decidability.Rewriting.Step`, an inductive type declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#step).

## Derivations in a string rewriting system

For a list of rules $R$, a word $x$ derives a
word $y$ when $x$ rewrites to $y$ in zero or more steps of $R$, that is, when $(x, y)$ lies in
the reflexive-transitive closure of the one-step rewriting relation of $R$.

Formalized by `Cslib.Decidability.Rewriting.Derives`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#derives).

## The reachability problem for string rewriting

An instance $(R, x, y)$ consists of a string
rewriting system $R$, given as a list of rules, and two words $x$ and $y$; it is a yes-instance of
the reachability problem when $x$ rewrites to $y$ in zero or more steps of $R$.

Formalized by `Cslib.Decidability.Rewriting.SR`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#sr).

## Rewriting systems with nonempty sides

A string rewriting system $R$, given as a list of
rules $(l, r)$, has nonempty sides when every rule of $R$ has a nonempty left side $l$ and a
nonempty right side $r$.

Formalized by `Cslib.Decidability.Rewriting.NonemptyRules`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#nonempty-rules).

## Lifting a word to the extended alphabet

A word $a_1 \cdots a_n$ over $\alpha$ is sent to
the word $a_1 \cdots a_n$ over the extended alphabet of $\alpha$ in which each $a_i$ is read as a
letter.

Formalized by `Cslib.Decidability.Rewriting.lift`, an abbreviation declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#lift).

## The start domino of the reduction from reachability to MPCP

Let $x$ be a word over an
alphabet $\alpha$, and extend $\alpha$ by a star $\star$ and an end marker $\diamond$. The start
domino of $x$ has top the one-letter word $\diamond$ and bottom the word $\diamond x \star$, with
the letters of $x$ read as letters of the extended alphabet.

Formalized by `Cslib.Decidability.Rewriting.startCard`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#start-card).

## Final domino

For a word $y$ over $\alpha$, the final domino of $y$ is the domino over the
extended alphabet with top $y \star \diamond$ and bottom $\diamond$, where $y$ is read as a word
of letters, $\star$ is the row separator and $\diamond$ is the end marker.

Formalized by `Cslib.Decidability.Rewriting.finalCard`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#final-card).

## The separator domino

Over the extended alphabet, that is, an alphabet $\alpha$ together
with a star $\star$ and an end marker $\diamond$, the separator domino has top and bottom both
equal to the one-letter word $\star$; the star separates the rows of a derivation.

Formalized by `Cslib.Decidability.Rewriting.sepCard`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#sep-card).

## The domino of a rewriting rule

For a rule $(l, r)$ over an alphabet $\alpha$, the domino
of the rule has top $l$ and bottom $r$, read as words over the extended alphabet, that is, $\alpha$
together with a star and an end marker.

Formalized by `Cslib.Decidability.Rewriting.ruleCard`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#rule-card).

## Copy domino

For a letter $a$ of $\alpha$, the copy domino of $a$ is the domino over the
extended alphabet whose top and bottom are both the one-letter word $a$.

Formalized by `Cslib.Decidability.Rewriting.copyCard`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#copy-card).

## Letters of a rewriting instance

For an instance $(R, x, y)$ of the reachability problem,
where $R = [(l_1, r_1), \dots, (l_k, r_k)]$ is a list of rewriting rules and $x$, $y$ are words,
the letters of the instance form the word $l_1 r_1 l_2 r_2 \cdots l_k r_k \, x \, y$, a list in
which a letter may occur several times.

Formalized by `Cslib.Decidability.Rewriting.symbols`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#symbols).

## The MPCP instance of a reachability instance

Let $(R, x, y)$ be an instance of the
reachability problem over an alphabet $\alpha$, where $R = [(l_1, r_1), \dots, (l_k, r_k)]$, and
write $\#$ for the separator and $\diamond$ for the end marker of the extended alphabet
$\mathrm{Sym}(\alpha)$, in which letters of $\alpha$ are read as letters. Let $a_1 \cdots a_m$ be
the word $l_1 r_1 l_2 r_2 \cdots l_k r_k \, x \, y$, the letters of the instance. The MPCP
instance of $(R, x, y)$ is the list of dominoes (top word, bottom word)
$(\diamond, \diamond x \#), (y \# \diamond, \diamond), (\#, \#), (l_1, r_1), \dots, (l_k, r_k),
(a_1, a_1), \dots, (a_m, a_m)$, in this order. Its first domino is $(\diamond, \diamond x \#)$.

Formalized by `Cslib.Decidability.Rewriting.toMPCP`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#to-mpcp).

## Letters differ from the star

For every letter $a$ of the alphabet $\alpha$, the symbol
$a$ of the extended alphabet of the MPCP-to-PCP reduction is different from the star $\star$.

Formalized by `Cslib.Decidability.Rewriting.letter_ne_star`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#letter-ne-star).

## Comparing words of letters before a separator

Let $u, v$ be words over $\alpha$, read as
words of letters, and let $X, Y$ be words over the extended alphabet of $\alpha$. If
$u X = v \star Y$, where $\star$ is the row separator, then there is a word $w$ over $\alpha$
with $v = u w$ and $X = w \star Y$.

Formalized by `Cslib.Decidability.Rewriting.exists_of_lift_append_eq`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#exists-of-lift-append-eq).

## The backward direction of the MPCP reduction

Let $(R, x, y)$ be a reachability instance
and read words over $\alpha$ as words of letters. Let $A$ be a sequence of dominoes of the MPCP
instance of $(R, x, y)$. For all words $v, s, t$ over $\alpha$, if $s$ rewrites to $t$ under $R$
in zero or more steps and the top of $A$ equals $v \star t$ followed by the bottom of $A$, where
$\star$ is the row separator, then $s v$ rewrites to $y$ under $R$ in zero or more steps.

Reading the dominoes left to right, $s$ is the part of the current row already matched, with
bottoms $t$, and $v$ is the rest of the row still to be matched on top.

Formalized by `Cslib.Decidability.Rewriting.derives_of_top_eq`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#derives-of-top-eq).

## Rewriting steps keep the letters of the instance

Let $(R, x, y)$ be an instance of the
reachability problem over an alphabet $\alpha$. If a word $w$ rewrites to a word $w'$ in one
step of $R$ and every letter of $w$ is among the letters of the instance, then every letter of
$w'$ is among the letters of the instance.

Formalized by `Cslib.Decidability.Rewriting.mem_symbols_of_step`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#mem-symbols-of-step).

## The forward direction of the MPCP reduction

Let $(R, x, y)$ be a reachability instance
and read words over $\alpha$ as words of letters. If a word $w$ over $\alpha$ rewrites to $y$
under $R$ in zero or more steps and every letter of $w$ occurs in a rule of $R$, in $x$ or in
$y$, then there is a sequence $A$ of dominoes of the MPCP instance of $(R, x, y)$ whose top is
$w \star$ followed by the bottom of $A$, where $\star$ is the row separator.

Formalized by `Cslib.Decidability.Rewriting.exists_cards_of_derives`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#exists-cards-of-derives).

## Reachability reduces to MPCP

For an instance $(R, x, y)$ of the reachability problem,
$x$ rewrites to $y$ in zero or more steps of $R$ if and only if the MPCP instance of $(R, x, y)$
has an MPCP solution, that is, a solution that starts with its first domino.

Formalized by `Cslib.Decidability.Rewriting.sr_iff_mpcp_toMPCP`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#sr-iff-mpcp-to-mpcp).

## The total reduction of reachability with nonempty sides to MPCP

On an instance
$(R, x, y)$ of the reachability problem, the reduction returns the MPCP instance of $(R, x, y)$
when every rule of $R$ has a nonempty left side and a nonempty right side, and otherwise the empty
list of dominoes, which has no solution.

Formalized by `Cslib.Decidability.Rewriting.reduce`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#reduce).

## Reachability with nonempty sides many-one reduces to MPCP with nonempty words

Let
$\alpha$ be an alphabet with a primitive recursive coding, and let $\alpha'$ be $\alpha$ extended
with two new symbols, the star and the end marker. There is a computable function $f$ from
instances $(R, x, y)$ of the reachability problem over $\alpha$, where $R$ is a list of rewriting
rules over $\alpha$ and $x$ and $y$ are words over $\alpha$, to finite lists of dominoes over
$\alpha'$ such that, for every such instance, the following are equivalent: every rule of $R$ has
a nonempty left side and a nonempty right side and $x$ rewrites to $y$ in zero or more steps of
$R$; and every domino of $f(R, x, y)$ has a nonempty top word and a nonempty bottom word and
$f(R, x, y)$ has an MPCP solution.

Formalized by `Cslib.Decidability.Rewriting.manyOneReducible_sr_mpcp`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#many-one-reducible-sr-mpcp).

## Reachability for rules with nonempty sides many-one reduces to PCP

Let $\alpha$ be an
alphabet with a primitive recursive coding, let $\alpha'$ be $\alpha$ extended with two new
symbols, the star and the end marker, and let $\alpha''$ be $\alpha'$ extended in the same way by
two further new symbols. There is a computable function $f$ from instances $(R, x, y)$ of the
reachability problem over $\alpha$, where $R$ is a list of rewriting rules over $\alpha$ and $x$
and $y$ are words over $\alpha$, to finite lists of dominoes over $\alpha''$ such that, for every
such instance, $f(R, x, y)$ has a PCP solution if and only if every rule of $R$ has a nonempty
left side and a nonempty right side and $x$ rewrites to $y$ in zero or more steps of $R$.

Formalized by `Cslib.Decidability.Rewriting.manyOneReducible_sr_pcp`, a theorem declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#many-one-reducible-sr-pcp).

## The word problem of a Thue system

On an instance $(R, x, y)$, where $R$ is a list of
rewriting rules and $x$, $y$ are words, the word problem asks whether $x$ and $y$ are related by
the equivalence relation generated by the one-step rewriting relation of $R$, that is, by its
reflexive, symmetric and transitive closure.

Formalized by `Cslib.Decidability.Rewriting.ThueWP`, a definition declared in [CSLibExt/Computability/Decidability/StringRewriting.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/StringRewriting.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html#thue-wp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: String rewriting systems](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/undecidable-problems/string-rewriting-systems)
