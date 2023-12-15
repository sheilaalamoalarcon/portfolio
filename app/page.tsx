import React from "react";
import styles from "./page.module.css";
import {
  workExperienceList,
  educationList,
  skills,
  idiomList,
  allProjects,
  aboutMe,
  menuIcon,
  envelopeIcon,
  linkedinIcon,
  artstationIcon,
} from "./lib/constanst";
import { SkillInfo, Project, List } from "./types/curriculum";
import SVGIcon from "./components/SVGIcon";

export default function Home() {
  function renderSkillStar(skillLevel: number) {
    return (
      <div>
        {Array.from({ length: skillLevel }).map((_, index) => (
          <svg
            key={index}
            xmlns="http://www.w3.org/2000/svg"
            width="15"
            height="15"
            viewBox="0 0 70 70"
            fill="none"
          >
            <path
              d="M32.1468 8.78114C33.0449 6.01721 36.9551 6.01722 37.8532 8.78115L42.1844 22.1115C42.5861 23.3475 43.7379 24.1844 45.0376 24.1844L59.0539 24.1844C61.9601 24.1844 63.1684 27.9033 60.8173 29.6115L49.4778 37.85C48.4264 38.614 47.9864 39.9681 48.388 41.2041L52.7193 54.5345C53.6174 57.2984 50.4539 59.5968 48.1028 57.8885L36.7634 49.65C35.7119 48.886 34.2881 48.886 33.2366 49.65L21.8972 57.8886C19.5461 59.5968 16.3826 57.2984 17.2807 54.5344L21.612 41.2041C22.0136 39.9681 21.5736 38.614 20.5221 37.85L9.18271 29.6115C6.83157 27.9032 8.0399 24.1844 10.9461 24.1844L24.9624 24.1844C26.2621 24.1844 27.4139 23.3475 27.8156 22.1115L32.1468 8.78114Z"
              fill="black"
            />
          </svg>
        ))}
      </div>
    );
  }

  function renderSkill(skills: SkillInfo[]) {
    return (
      <div className={styles.skillsGrid}>
        {skills.map((skill) => (
          <div className={styles.rowWrap}>
            <p>{skill.name}</p>
            {renderSkillStar(skill.level)}
          </div>
        ))}
      </div>
    );
  }

  function renderProject(projects: Project[]) {
    return projects.map((project) => (
      <section className={styles.sectionBody}>
        <h4>{project.title}</h4>
        <p>{project.body}</p>
        <div className={styles.rowWrap}>
          <h5>Technologies</h5>
          <p>{project.stack}</p>
        </div>
        <div className={styles.rowWrap}>
          <h5>Role</h5>
          <p>{project.role}</p>
        </div>
      </section>
    ));
  }

  function renderList(list: List) {
    return (
      <div>
        <h3>{list.title}</h3>
        <ul className={styles.sectionBody}>
          {list.body.map((item) => (
            <li>{item}</li>
          ))}
        </ul>
      </div>
    );
  }

  return (
    <>
      <header className={styles.header}>
        <SVGIcon
          width={menuIcon.width}
          height={menuIcon.height}
          viewBox={menuIcon.viewBox}
          path={menuIcon.path}
        />
        <h1>Sheila's Portfolio</h1>
        <div className={styles.headerIcons}>
          <a href="mailto:sheilaalamoalarcon@gmail.com">
            <SVGIcon
              width={envelopeIcon.width}
              height={envelopeIcon.height}
              viewBox={envelopeIcon.viewBox}
              path={envelopeIcon.path}
            />
          </a>
          <a href="https://www.linkedin.com/in/sheila-álamo/">
            <SVGIcon
              width={linkedinIcon.width}
              height={linkedinIcon.height}
              viewBox={linkedinIcon.viewBox}
              path={linkedinIcon.path}
            />
          </a>
          <SVGIcon
            width={artstationIcon.width}
            height={artstationIcon.height}
            viewBox={artstationIcon.viewBox}
            path={artstationIcon.path}
          />
        </div>
      </header>
      <main className={styles.main}>
        <div className={styles.curriculum}>
          <div>
            <h2>Curriculum</h2>
            <div className={styles.nameAndWorkTitleWrap}>
              <p>Sheila Alamo</p>
              <p className={styles.workTitle}>
                Junior Mobile Application Developer
              </p>
            </div>
            <section>
              <h3>About Me</h3>
              <p className={styles.sectionBody}>{aboutMe}</p>
            </section>
            {renderList(workExperienceList)}
            {renderList(educationList)}
            {renderList(idiomList)}
          </div>
          <div>
            <div>
              <h3>Skills</h3>
              <h4>Languages</h4>
              {renderSkill(skills.hardSkills.languages)}
              <h4>Frameworks/Libraries</h4>
              {renderSkill(skills.hardSkills.frameworks)}
            </div>
            <div>
              <h3>Soft Skills</h3>
              {renderSkill(skills.softSkills)}
            </div>
          </div>
        </div>
        <div>
          <h3>Latest Projects</h3>
          {renderProject(allProjects)}
        </div>
      </main>
    </>
  );
}
