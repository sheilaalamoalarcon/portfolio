export interface SkillInfo {
  name: string;
  level: number;
}

export interface Skills {
  hardSkills: {
    languages: SkillInfo[];
    frameworks: SkillInfo[];
  };
  softSkills: SkillInfo[];
}
export interface Project {
  title: string;
  body: string;
  stack: string;
  role: string;
}
export interface List {
  title: string;
  body: string[];
}
