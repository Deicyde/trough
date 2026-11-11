---
declaration: section
origin: cited
lean: Cslib.Crypto.Birthday.collisionGame, Cslib.Crypto.Birthday.collisionProb, Cslib.Crypto.Birthday.collisionProb_eq, Cslib.Crypto.Birthday.collisionProb_le, Cslib.Crypto.Birthday.one_sub_exp_le_collisionProb, Cslib.Crypto.Birthday.div_one_add_le_collisionProb, Cslib.Crypto.Birthday.collisionProb_ge, Cslib.Crypto.Birthday.collisionProb_ge_of_le_sqrt
statement: formalized
proof: formalized
---

# Birthday bound

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html).

## The collision experiment

For a nonempty finite set $\alpha$ and a natural number $q$, the
collision experiment is the probability distribution on $\{\mathrm{true}, \mathrm{false}\}$
obtained by drawing a function $s \colon \{0, \dots, q - 1\} \to \alpha$ uniformly at random
(equivalently, $q$ independent uniform samples $s(0), \dots, s(q - 1)$ from $\alpha$) and
outputting true exactly when $s$ is not injective, that is, when $s(i) = s(j)$ for some
$i \ne j$.

Formalized by `Cslib.Crypto.Birthday.collisionGame`, a definition declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#collision-game).

## Collision probability

For a nonempty finite set $\alpha$ and a natural number $q$, the
collision probability is the probability, as a real number, that the collision experiment with
$q$ samples from $\alpha$ outputs true, that is, that $q$ independent uniform samples from
$\alpha$ contain two equal samples at distinct positions.

Formalized by `Cslib.Crypto.Birthday.collisionProb`, a definition declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#collision-prob).

## The exact collision probability

Let $\alpha$ be a nonempty finite set with $N$ elements
and $q$ a natural number. The probability that $q$ independent uniform samples from $\alpha$
contain a collision equals $1 - N (N - 1) \cdots (N - q + 1) / N^q$, where the product
$N (N - 1) \cdots (N - q + 1)$ has $q$ factors (it is $1$ for $q = 0$ and $0$ for $q > N$).

Formalized by `Cslib.Crypto.Birthday.collisionProb_eq`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#collision-prob-eq).

## Birthday upper bound

Let $\alpha$ be a nonempty finite set with $N$ elements and $q$ a
natural number. The probability that $q$ independent uniform samples from $\alpha$ contain a
collision is at most $q (q - 1) / (2 N)$.

This implies Katz and Lindell's Lemma A.15, which states the bound $q^2 / (2 N)$.

Formalized by `Cslib.Crypto.Birthday.collisionProb_le`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#collision-prob-le).

## Birthday lower bound, exponential form

Let $\alpha$ be a nonempty finite set with $N$
elements and $q$ a natural number. The probability that $q$ independent uniform samples from
$\alpha$ contain a collision is at least $1 - \exp(-q (q - 1) / (2 N))$.

Formalized by `Cslib.Crypto.Birthday.one_sub_exp_le_collisionProb`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#one-sub-exp-le-collision-prob).

## Birthday lower bound, rational form

Let $\alpha$ be a nonempty finite set with $N$
elements, $q$ a natural number, and $x = q (q - 1) / (2 N)$. The probability that $q$ independent
uniform samples from $\alpha$ contain a collision is at least $x / (1 + x)$.

Formalized by `Cslib.Crypto.Birthday.div_one_add_le_collisionProb`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#div-one-add-le-collision-prob).

## Birthday lower bound

Let $\alpha$ be a nonempty finite set with $N$ elements and $q$ a
natural number with $q (q - 1) \le 2 N$. The probability that $q$ independent uniform samples
from $\alpha$ contain a collision is at least $q (q - 1) / (4 N)$.

This strengthens Katz and Lindell's Lemma A.16, whose hypothesis $q \le \sqrt{2 N}$ implies
$q (q - 1) \le 2 N$.

Formalized by `Cslib.Crypto.Birthday.collisionProb_ge`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#collision-prob-ge).

## Birthday lower bound as stated in Katz and Lindell

Let $\alpha$ be a nonempty finite set
with $N$ elements and $q$ a natural number with $q \le \sqrt{2 N}$. The probability that $q$
independent uniform samples from $\alpha$ contain a collision is at least $q (q - 1) / (4 N)$.

This is Lemma A.16 of Katz and Lindell (2nd ed.): "say $q \le \sqrt{2N}$ elements are chosen
uniformly and independently ... at least $q (q - 1) / (4N)$".

Formalized by `Cslib.Crypto.Birthday.collisionProb_ge_of_le_sqrt`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#collision-prob-ge-of-le-sqrt).

## Birthday lower bound for at most square-root many samples

Let $\alpha$ be a nonempty
finite set with $N$ elements and $q$ a natural number with $q \le \sqrt{N}$. The probability that
$q$ independent uniform samples from $\alpha$ contain a collision is at least
$q (q - 1) / (4 N)$.

Formalized by `Cslib.Crypto.Birthday.collisionProb_ge_of_le_sqrt_card`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#collision-prob-ge-of-le-sqrt-card).

## Even odds of a collision

Let $\alpha$ be a nonempty finite set with $N$ elements and $q$ a
natural number with $2 N \le q (q - 1)$. The probability that $q$ independent uniform samples from
$\alpha$ contain a collision is at least $1/2$.

Formalized by `Cslib.Crypto.Birthday.half_le_collisionProb`, a theorem declared in [CSLibExt/Crypto/Hash/Birthday.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Hash/Birthday.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html#half-le-collision-prob).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Birthday bound](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/birthday-bound/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/cryptography/birthday-bound)
